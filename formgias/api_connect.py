from __future__ import unicode_literals
from frappeclient import FrappeClient
import frappe

import json

import socket

from frappe.model.document import Document

class api_connect(Document):
	pass


@frappe.whitelist()
def sync_permintaan_barang():
	clientroot = FrappeClient("http://139.59.125.102/", "administrator", "doremi123")
	sumber_po = clientroot.get_doc("Permintaan Barang fg")

	selip = ""
	first = True
	hasil_akhir = ""
	counter = 0

	for row in sumber_po:
		if row["name"]:
			if first:
				first = False
				selip =  """ SELECT "{}" test_value """.format(row["name"]) + selip
			else :
				selip =  """ SELECT "{}" test_value UNION """.format(row["name"]) + selip

	if selip != "":
		hasil_akhir = frappe.db.sql(""" SELECT * FROM ({}) a WHERE a.test_value NOT IN (SELECT name FROM `tabPermintaan Barang fg`) """.format(selip),as_list=1)	
	
	if hasil_akhir:
		for row in hasil_akhir:		
			patokan_po_baru = clientroot.get_doc("tabPermintaan Barang fg",str(row[0]))
			if str((patokan_po_baru["docstatus"])) == "1":		
					pr_doc = frappe.new_doc("tabPermintaan Barang fg")
					# frappe.throw(patokan_po_baru.get("name"))

					kolom_parent = frappe.db.sql(""" SELECT COLUMN_NAME
									FROM INFORMATION_SCHEMA.COLUMNS
									WHERE TABLE_NAME='tabPermintaan Barang fg' """)

					for rowkolom in kolom_parent:
						if str(rowkolom[0]) != "notification_email_address" and str(rowkolom[0]) != "docstatus" and str(patokan_po_baru.get(str(rowkolom[0]))) != "None":
							pr_doc.update({ str(rowkolom[0]) : patokan_po_baru.get(str(rowkolom[0])) })
					
					pr_doc.update({ "write_off_account" : "Write Off - GIAS" })

					for temp_baris_item in patokan_po_baru.get("detail") :
						baris_item = pr_doc.append("detail")
						baris_item.item_code = temp_baris_item["item_code"]
						baris_item.item_name = temp_baris_item["item_name"]
						baris_item.item_description = temp_baris_item["item_description"]
						baris_item.qty = temp_baris_item["qty"]
						baris_item.uom = temp_baris_item["uom"]
						baris_item.employee = temp_baris_item["employee"]
						baris_item.department = temp_baris_item["department"]
						

					pr_doc.flags.ignore_permissions = 1
					pr_doc.save()
					# pr_doc.submit()
					frappe.db.commit()
					counter = counter + 1

					# if frappe.get_doc("Purchase Invoice", str(patokan_po_baru.get("name"))):
					# 	patokan_po_baru["tax_document"] = str(patokan_po_baru.get("name"))
					# 	clientroot.update(patokan_po_baru)

					submit_doc = frappe.get_doc("Permintaan Barang fg",patokan_po_baru["name"])
					submit_doc.submit()
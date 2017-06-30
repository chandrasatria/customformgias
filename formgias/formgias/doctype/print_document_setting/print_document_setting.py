# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bobby and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PrintDocumentSetting(Document):
	pass

@frappe.whitelist()
def check_doc(dt,dn):
	result = frappe.db.sql(""" SELECT pdoc.`name` FROM `tabPrint Document Setting`pdoc 
		WHERE pdoc.`doctype_name`="{0}" AND pdoc.`document_name`="{1}" """.format(dt,dn),as_list=1)
	if result :
		return "NO"
	else :
		doc = frappe.new_doc("Print Document Setting")
		doc.doctype_name = dt
		doc.document_name = dn
		doc.save()
		return "OK"
	
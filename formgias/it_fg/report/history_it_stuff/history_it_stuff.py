# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []

	where_it_asset = ""

	if filters.get("tipe") == "Serah Terima":
		if filters.get("it_asset"):
			where_it_asset = """ AND rii.ti_asset = "{}" """.format(filters.get("it_asset"))
		
		columns = ["Tanggal Request:Date:100",
					"IT Asset:Link/IT Asset fg:100",
					"Estimation Price:Currency:150",
					"Qty:Float:100",
					"Description:Data:200",
					"Status:Data:100"]

		data = frappe.db.sql(""" SELECT 
				ri.tanggal_request AS tanggal, 
				rii.it_asset AS item, 
				rii.estimation_price AS cost, 
				rii.qty AS qty, 
				rii.description AS description,
				IF(rii.qty>0,"Barang Masuk","Barang Keluar") AS statu

				FROM `tabRequest IT Stuff fg` ri JOIN `tabRequest IT Stuff Item Detail fg` rii ON rii.parent= ri.name
				WHERE ri.workflow_state = "Completed" {}
				ORDER BY ri.tanggal_request; """.format(where_it_asset))

	if filters.get("tipe") == "Request IT Stuff":
		if filters.get("it_asset"):
			where_it_asset = """ AND sti.nama_asset = "{}" """.format(filters.get("it_asset"))
		
		columns = ["Tanggal Serah Terima:Date:100",
					"IT Asset:Link/IT Asset fg:100",
					"Cost Price:Currency:150",
					"Remark:Data:200",
					"Dari Employee:Data:100",
					"Ke Employee:Data:100"]

		data = frappe.db.sql(""" SELECT 
				st.tanggal_serah_terima AS tanggal,
				sti.nama_asset,
				sti.cost,
				sti.remark,
				te1.employee_name,
				te2.employee_name

				FROM `tabSerah Terima fg` st JOIN `tabItem Details fg` sti ON st.name = sti.parent
				LEFT JOIN `tabEmployee` te1 ON te1.name = st.from_employee
				LEFT JOIN `tabEmployee` te2 ON te2.name = st.to_employee

				WHERE st.workflow_state = "Completed" {}
				ORDER BY st.tanggal_serah_terima""".format(where_it_asset))

	return columns, data

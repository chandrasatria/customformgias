// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.query_reports["History IT Stuff"] = {
	"filters": [
		{
			"fieldname":"it_asset",
			"label": __("IT Asset"),
			"fieldtype": "Link",
			"options": "IT Asset fg"
		},
		{
			"fieldname":"tipe",
			"label": __("Tipe"),
			"fieldtype": "Select",
			"options": ["Serah Terima","Request IT Stuff"],
			"reqd": 1,
			"default": "Serah Terima"
		},
	]
}

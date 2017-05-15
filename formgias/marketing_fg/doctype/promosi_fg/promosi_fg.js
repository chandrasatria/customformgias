// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Promosi fg', {
	refresh: function(frm) {
		cur_frm.add_fetch("item_code","item_name","item_name")

		frappe.ui.form.on("Promosi Budget List fg", "budget", function(frm, cdt, cdn) {

		   var material_details = frm.doc.budget_list
		   var jumlah = 0
		   for(var i in material_details) {
				jumlah = jumlah + material_details[i].budget
			}

			frm.set_value("total_budget",jumlah)
		});

		frappe.ui.form.on("Promosi Estimation Profit List fg", "profit", function(frm, cdt, cdn) {

		   var material_details1 = frm.doc.estimation_profit_list
		   var jumlah1 = 0
		   var jumlah2 = 0
		   for(var i in material_details1) {
				jumlah1 = jumlah1 + material_details1[i].omzet
				jumlah2 = jumlah2 + material_details1[i].profit
			}

			frm.set_value("total_omset",jumlah1)
			frm.set_value("total_profit",jumlah2)
		});

		frappe.ui.form.on("Promosi fg", "total_profit", function(frm, doctype, name) {

		  		var row = locals[doctype][name];
				row.percentage_profit=(row.total_profit/row.total_omset)*100;
				refresh_field("percentage_profit");
		});

	}
});

// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('P and D Request Form fg', {
	refresh: function(frm) {

		cur_frm.add_fetch("request_by","company","company")
		cur_frm.add_fetch("request_by","branch","branch")

		frappe.ui.form.on("P and D Request Form Item", "total", function(frm, cdt, cdn) {

		   var material_details = frm.doc.items
		   var jumlah = 0
		   for(var i in material_details) {
			jumlah = jumlah + material_details[i].total
			}

			frm.set_value("grand_total",jumlah)
		});


	}
});

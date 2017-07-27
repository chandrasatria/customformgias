// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Request IT Stuff fg', {
	refresh: function(frm) {

	}
});
cur_frm.cscript.custom_it_asset = function(doc,cdt,cdn){
	tabel = locals[cdt][cdn]

	frappe.call({
		method:"erpnext.selling.custom_method.get_current_qty_it_asset",
		args:{
			asset_code: tabel.it_asset
		},
		callback: function(r){
			tabel.current_qty = r.message
			refresh_field("current_qty")
		}
	});
}

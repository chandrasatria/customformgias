// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('IT Asset fg', {
	refresh: function(doc) {
		
	}
});

cur_frm.cscript.custom_refresh = function(doc){
	if (!doc.__islocal){
		frappe.call({
			method:"erpnext.selling.custom_method.get_current_qty_it_asset",
			args:{
				asset_code: cur_frm.doc.referensi_item
			},
			callback: function(r){
				doc.current_stock = (r.message)
				refresh_field("current_stock")
			}
		});
	}
}
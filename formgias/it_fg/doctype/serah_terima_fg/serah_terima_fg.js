// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Serah Terima fg', {
	refresh: function(frm) {

		cur_frm.add_fetch("it_asset","asset_name","nama_asset")
		cur_frm.add_fetch("it_asset","no_seri","no_seri_asset")

	}
});

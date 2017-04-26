// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Promosi fg', {
	refresh: function(frm) {
		cur_frm.add_fetch("item_code","item_name","item_name")

	}
});

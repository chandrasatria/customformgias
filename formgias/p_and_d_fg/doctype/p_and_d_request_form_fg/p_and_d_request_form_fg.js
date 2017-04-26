// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('P and D Request Form fg', {
	refresh: function(frm) {

		cur_frm.add_fetch("request_by","company","company")
		cur_frm.add_fetch("request_by","branch","branch")


	}
});

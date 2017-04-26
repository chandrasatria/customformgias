// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pengajuan SP fg', {
	refresh: function(frm) {

		cur_frm.add_fetch("employee","employee_name","employee_name")
		cur_frm.add_fetch("employee","designation","jabatan")

	}
});

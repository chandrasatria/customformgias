// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pengajuan Perubahan Jabatan Karyawan fg', {
	refresh: function(frm) {

		cur_frm.add_fetch("employee","designation","current_designation")

	}
});

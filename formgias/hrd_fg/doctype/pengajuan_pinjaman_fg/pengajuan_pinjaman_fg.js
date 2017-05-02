// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pengajuan Pinjaman fg', {
	refresh: function(frm) {

			cur_frm.add_fetch("employee","employee_name","employee_name")
			cur_frm.add_fetch("employee","designation","designation")
			cur_frm.add_fetch("employee","department","department")
			cur_frm.add_fetch("employee","company","company")
			cur_frm.add_fetch("employee","passport_number","no_ktp")
			cur_frm.add_fetch("employee","date_of_joining","entry_date")

			frappe.ui.form.on("Pengajuan Pinjaman fg","entry_date",function(){
				cur_frm.doc.masa_kerja = frappe.datetime.get_day_diff(cur_frm.doc.today,cur_frm.doc.entry_date);
				refresh_field("masa_kerja");
			});

	}
});

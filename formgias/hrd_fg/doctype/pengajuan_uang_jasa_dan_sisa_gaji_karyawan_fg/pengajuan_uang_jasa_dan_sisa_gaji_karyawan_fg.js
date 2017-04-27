// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pengajuan Uang Jasa dan Sisa Gaji Karyawan fg', {
	refresh: function(frm) {
		//cur_frm.cscript.custom_validate = function(doc) {
		frappe.ui.form.on("Pengajuan Uang Jasa dan Sisa Gaji Karyawan fg","sisa_kewajiban",function(frm, doctype, name){
			//if (cur_frm.doc.nominal != '' && cur_frm.doc.hutang_karyawan != '' && cur_frm.doc.sisa_kewajiban !='' ){
				var row = locals[doctype][name];
				row.net=row.nominal-(row.hutang_karyawan+row.sisa_kewajiban);
				refresh_field("net");
			//}
		});

		frappe.ui.form.on("Pengajuan Uang Jasa dan Sisa Gaji Karyawan fg","quit_date",function(){
			cur_frm.doc.lama_kerja = frappe.datetime.get_day_diff(cur_frm.doc.quit_date,cur_frm.doc.entry_date);
			refresh_field("lama_kerja");
		});

		
	}
});

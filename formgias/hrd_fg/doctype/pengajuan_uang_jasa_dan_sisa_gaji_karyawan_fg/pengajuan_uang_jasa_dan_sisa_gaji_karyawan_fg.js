// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pengajuan Uang Jasa dan Sisa Gaji Karyawan fg', {
	refresh: function(frm) {
		//cur_frm.cscript.custom_validate = function(doc) {
		frappe.ui.form.on("Pengajuan Uang Jasa dan Sisa Gaji Karyawan fg","nominal",function(){
			//if (cur_frm.doc.nominal != '' && cur_frm.doc.hutang_karyawan != '' && cur_frm.doc.sisa_kewajiban !='' ){
				cur_frm.doc.net=cur_frm.doc.nominal-(cur_frm.doc.hutang_karyawan+cur_frm.doc.sisa_kewajiban);
				refresh_field("net");
			//}
		});

		frappe.ui.form.on("Pengajuan Uang Jasa dan Sisa Gaji Karyawan fg","quit_date",function(){
			cur_frm.doc.lama_kerja = frappe.datetime.get_day_diff(cur_frm.doc.quit_date,cur_frm.doc.entry_date);
			refresh_field("lama_kerja");
		});

		// frappe.ui.form.on("Pengajuan Uang Jasa dan Sisa Gaji Karyawan fg", "entry_date", function(frm, cdt, cdn) {
		// 	var z = locals[cdt][cdn];

		// 	if(z.entry_date && z.quit_date) {
		// 		lama_kerja = frappe.datetime.get_date_hours(z.quit_date, z.entry_date);
		// 		frappe.model.set_value(cdt, cdn, "lama_kerja", lama_kerja);
		// 		cur_frm.refresh();
		// 	}
		// });

	}
});

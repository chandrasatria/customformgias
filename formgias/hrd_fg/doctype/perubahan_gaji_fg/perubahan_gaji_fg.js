// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Perubahan Gaji fg', {
	refresh: function(frm) {
		cur_frm.add_fetch("employee","employee_name","employee_name")

		frappe.ui.form.on("Perubahan Gaji fg","uang_yang_diajukan",function(frm, doctype, name){
			//if (cur_frm.doc.nominal != '' && cur_frm.doc.hutang_karyawan != '' && cur_frm.doc.sisa_kewajiban !='' ){
				var row = locals[doctype][name];
				row.total_kenaikan=(row.gaji_pokok_yang_diajukan-row.gaji_pokok_saat_ini)+(row.tunjangan_yang_diajukan+row.tunjangan_saat_ini)+(row.uang_yang_diajukan-row.uang_makan_saat_ini);
				refresh_field("total_kenaikan");
			//}
		});


	}
});

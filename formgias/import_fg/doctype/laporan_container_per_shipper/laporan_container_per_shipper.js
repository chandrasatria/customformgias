// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Laporan Container per Shipper', {
	refresh: function(frm) {
		frappe.ui.form.on("Kota dan Bulan fg","desember",function(frm, cdt, cdn){
			//if (cur_frm.doc.nominal != '' && cur_frm.doc.hutang_karyawan != '' && cur_frm.doc.sisa_kewajiban !='' ){
				var row = locals[cdt][cdn];
				row.total=row.januari+row.februari+row.maret+row.april+row.mei+row.juni+row.juli+row.agustus+row.september+row.oktober+row.november+row.desember;
				refresh_field("total");
			//}
		});

	}
});

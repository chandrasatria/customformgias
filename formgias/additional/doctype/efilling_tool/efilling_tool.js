// Copyright (c) 2016, Bobby and contributors
// For license information, please see license.txt

frappe.ui.form.on('EFilling Tool', {
	refresh: function(frm) {

	}
});


//custom script

//frappe.ui.form.on('Get Data Pajak Keluaran', {
//   get_data_pajak_keluaran_remove: function(frm) {
//	frappe.throw("Hai");
//	msgprint("Halo");
//	console.log("Hey dude, you added something to booked !!!")
//   	var d = locals[cdt][cdn]
//       frappe.call({
//		method: "gias.additional_tools.doctype.efilling_tool.efilling_tool.delete_pajak_keluar_ite",
//	
//		args: {
//			"referensi": d["referensi"],
//			"name":d["name"]
		
//		},
//		callback: function(r) {
//			msgprint(r["message"]);
//			refresh_field("get_data_item_pajak_sales_invoice");
//		}
//	})

//    }
//});


// frappe.ui.form.on('Get Data Pajak Keluaran', {
//   get_data_pajak_keluaran_remove: function(frm,cdt,cdn) {

// 		var d = locals[cdt][cdn]
		
// 		var tbl = frm.doc.get_data_item_pajak_sales_invoice || [];
// 		var i = tbl.length;
// 		while (i--)
// 		{
// 		    if(tbl[i].sales_invoice == d["referensi"])
// 		    {
// 		        cur_frm.get_field("get_data_item_pajak_sales_invoice").grid.grid_rows[i].remove();
// 		    }
// 		}
// 		cur_frm.refresh();


//   }
// });




// frappe.ui.form.on('Get Data Pajak Keluaran', {
//    get_data_pajak_keluaran_remove: function(frm) {
	

// 	var table_temp = []
// 	for (row in frm.doc.get_data_pajak_keluaran){
// 	  for(x in frm.doc.get_data_item_pajak_sales_invoice){	
// 		if(frm.doc.get_data_pajak_keluaran[row].referensi!=frm.doc.get_data_item_pajak_sales_invoice[x].sales_invoice){
		
// 		table_temp.push(frm.doc.get_data_item_pajak_sales_invoice[x])	
// 		}
// 	  }
	
// 	}
// 	cur_frm.clear_table("get_data_item_pajak_sales_invoice");
// 	frm.doc.get_data_item_pajak_sales_invoice = table_temp
// 	refresh_field("frm.doc.get_data_item_pajak_sales_invoice")
// 	refresh_field("frm.doc.get_data_pajak_keluaran")
// }	

// });


cur_frm.cscript.print_to_excel= function(doc, cdt, cdn) {
	
        $c_obj_csv(doc, 'print_to_excel', '', '');
  
}

frappe.query_reports["EFilling Tool"] = {
	"filters": [
		{
			"fieldname": "tanggal_faktur",
			"label": __("Tanggal"),
			"fieldtype": "Date",
			"width": "80",
			"default": frappe.datetime.get_today()
		},

		]
}
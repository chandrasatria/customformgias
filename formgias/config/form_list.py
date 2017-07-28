from __future__ import unicode_literals
from frappe import _
import frappe

def get_data():

	return [
			{
				"label": _("IT"),
				"items": [
					{
						"type": "doctype",
						"name": "IT Asset Category fg",
					},
					{
						"type": "doctype",
						"name": "IT Asset fg",
					},
					{
						"type": "doctype",
						"name": "IT Stuff Main Category",
					},
					{
						"type": "doctype",
						"name": "IT Stuff Request Category fg",
					},
					{
						"type": "doctype",
						"name": "Request IT Stuff fg",
					},
					{
						"type": "doctype",
						"name": "Serah Terima fg",
					},
					{
						"type": "report",
						"name": "History IT Stuff",
					},
				]
			},
			{
				"label": _("Logistic"),
				"items": [
					{
						"type": "doctype",
						"name": "Insurance Request fg",
					},
					{
						"type": "doctype",
						"name": "Request Logistic Vehicle fg",
					},
					{
						"type": "doctype",
						"name": "Vehicle Log fg",
					},
				]
			},
			{
				"label": _("Marketing"),
				"items": [
					{
						"type": "doctype",
						"name": "Permintaan Kas fg",
					},
					{
						"type": "doctype",
						"name": "Promosi fg",
					},
					{
						"type": "doctype",
						"name": "Realisasi Insentif fg",
					},
				]
			},
			{
				"label": _("CS"),
				"items": [
					{
						"type": "doctype",
						"name": "Product Complain fg",
					},
					{
						"type": "doctype",
						"name": "Request Kredit Limit fg",
					},
				]
			},
			{
				"label": _("Audit"),
				"items": [
					{
						"type": "doctype",
						"name": "Request Write Off Account fg",
					},
					{
						"type": "doctype",
						"name": "Request Write Off AR fg",
					},
				]
			},
			{
				"label": _("HRD"),
				"items": [
					{
						"type": "doctype",
						"name": "Description Appraisal fg",
					},
					{
						"type": "doctype",
						"name": "Description Appraisal Template fg",
					},
					{
						"type": "doctype",
						"name": "Pengajuan Asuransi dan BPJS fg",
					},
					{
						"type": "doctype",
						"name": "Pengajuan Pinjaman fg",
					},
					{
						"type": "doctype",
						"name": "Pengajuan SP fg",
					},
					{
						"type": "doctype",
						"name": "Pengajuan Uang Jasa dan Sisa Gaji Karyawan fg",
					},
					{
						"type": "doctype",
						"name": "Perubahan Gaji fg",
					},
					{
						"type": "doctype",
						"name": "Sumbangan fg",
					},
				]
			},
			{
				"label": _("P and D"),
				"items": [
					{
						"type": "doctype",
						"name": "P and D Event fg",
					},

					{
						"type": "doctype",
						"name": "P and D Request Form fg",
					},
				]
			},
			{
				"label": _("B and D"),
				"items": [
					{
						"type": "doctype",
						"name": "B and D Request Document fg",
					},
					{
						"type": "doctype",
						"name": "B and D Request fg",
					},
				]
			},
			{
				"label": _("Finance"),
				"items": [
					{
						"type": "doctype",
						"name": "Giro fg",
					},
					{
						"type": "doctype",
						"name": "Payment Requests fg",
					},
				]
			},
			{
				"label": _("P and GA"),
				"items": [
					{
						"type": "doctype",
						"name": "Category Permintaan fg",
					},
					{
						"type": "doctype",
						"name": "Permintaan Barang fg",
					},
				]
			},
			{
				"label": _("Import"),
				"items": [
					{
						"type": "doctype",
						"name": "Laporan Container per Shipper",
					},
					{
						"type": "doctype",
						"name": "Laporan Realisasi fg",
					},
					{
						"type": "doctype",
						"name": "Laporan Shipment dan Kontainer fg",
					},
					{
						"type": "doctype",
						"name": "Laporan untuk Import Shipment fg",
					},
					{
						"type": "doctype",
						"name": "Rekap Jumlah Container per Shipper",
					},
					{
						"type": "doctype",
						"name": "Rekap Shipment",
					},
				]
			},
			{
				"label": _("Coaching"),
				"items": [
					{
						"type": "doctype",
						"name": "Coaching Form fg",
					},
				]
			},
		]

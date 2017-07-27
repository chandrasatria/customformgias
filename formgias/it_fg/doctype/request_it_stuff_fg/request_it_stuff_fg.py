# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RequestITStufffg(Document):
	def validate(self):
		for row in self.item_detail:
			if row.qty + row.current_qty < 0:
				frappe.throw("Maaf, qty yang anda request untuk keluar melebihi jumlah barang saat ini. Silahkan cek pada baris item {}".format(row.it_asset))

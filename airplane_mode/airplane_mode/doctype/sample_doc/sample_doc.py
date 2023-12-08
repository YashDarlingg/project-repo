# Copyright (c) 2023, Airplane and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class sampledoc(Document):
	# doc=frappe.get_doc({
	# 	'doctype':'Sample doc2',
	# })
	# x=frappe.new_doc("Sample doc2")
	# x.fname="abc"
	# x.sname="abc"
	# x.ffname="abc"
	# x.insert()
	
	doc=frappe.get_list("Airplane ticket",
		

		
		fields=['passenger','flight']
	)
	print(doc)
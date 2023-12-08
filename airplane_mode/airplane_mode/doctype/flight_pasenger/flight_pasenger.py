import frappe
from frappe.model.document import Document

class Flightpasenger(Document):
    def before_save(self):
        self.full_name = f"{self.first_name} {self.last_name}"
   





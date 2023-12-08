import frappe
import random
from frappe.model.document import Document

class Airplaneticket(Document):
    def before_save(self):
        if self.status!="Boarded":
            frappe.throw("status should be borded")
        total=0
        add_on_list = self.get("add_on") or []
        for item in add_on_list:
           total= total+(item.amount)   
        self.total_amount=self.flight_price + total

        # num = random.randint(10, 100)
        # strng=random.choice(["A","B","c","D","E"])
        # self.seat_value= f"{num}{strng}"
        # self.seat=self.seat_value
    
    def validate(self):
        self.add_on_type=[]
        add_ons = self.get("add_on") or []
        unique_types = set()
        unique_add_ons = []

        for add_on in add_ons:
            add_on_type = add_on.item


            if add_on_type not in unique_types:
                unique_types.add(add_on_type)
                unique_add_ons.append(add_on)
            else:
                frappe.throw(f"Duplicate add-on type '{add_on_type}' found.")

            if add_on_type is None:
                frappe.throw("Add-on type cannot be None.")

        self.set("add_on", unique_add_ons)



        capacity = frappe.get_value("Airplane", self.flight, "capacity")

        ticket_count = frappe.db.count("Airplane ticket", {"flight": self.flight, "docstatus": 1})

        if ticket_count >= capacity:
            frappe.throw(("The number of tickets for this flight has reached its capacity. Cannot create a new ticket"))


        # if self.docstatus == 0:
        #     airplane_capacity = frappe.get_value("Airplane ticket", self.flight, "capacity")
        #     ticket_count = frappe.db.count("Airplane ticket", {"Airplane ticket": self.flight, "docstatus": 1})

        #     if ticket_count >= airplane_capacity:
        #         frappe.throw(_("The number of tickets for this flight has reached its capacity. Cannot create a new ticket"))



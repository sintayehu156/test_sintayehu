# Copyright (c) 2024, sintayehu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PowerConsumptionData(Document):
    # Assigns a unique counter value for the customer before inserting the document.
    def before_insert(self):
        if self.customer:
            # Get the maximum counter value for this customer
            last_entry = frappe.get_all("Power Consumption Data",
                filters={"customer": self.customer},
                fields=["customer_entry_counter"],
                order_by="customer_entry_counter desc",
                limit=1
            )
            if last_entry:
                self.customer_entry_counter = last_entry[0].get('customer_entry_counter') + 1
            else:
                self.customer_entry_counter = 1

    def autoname(self):
        self.name = f"{self.customer}-{self.customer_entry_counter:04d}"

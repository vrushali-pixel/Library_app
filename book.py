import frappe
from frappe.model.document import Document

class Book(Document):
    def validate(self):
        if self.isbn and len(self.isbn) != 13:
            frappe.throw("ISBN must be exactly 13 characters long.")

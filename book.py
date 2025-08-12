import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class Book(Document):
    def validate(self):
        if len(self.isbn) != 13:
            frappe.throw("ISBN must be exactly 13 characters long.")

    def autoname(self):
	self.name = make_autoname("BOOK-.#####")

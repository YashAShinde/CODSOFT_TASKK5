import tkinter as tk
from tkinter import messagebox

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")

        self.contacts = []

        # Labels
        self.label_name = tk.Label(root, text="Name:")
        self.label_phone = tk.Label(root, text="Phone:")
        self.label_email = tk.Label(root, text="Email:")
        self.label_address = tk.Label(root, text="Address:")

        # Entry widgets
        self.entry_name = tk.Entry(root)
        self.entry_phone = tk.Entry(root)
        self.entry_email = tk.Entry(root)
        self.entry_address = tk.Entry(root)

        # Buttons
        self.button_add = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.button_view = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.button_search = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.button_update = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.button_delete = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Grid layout
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.label_phone.grid(row=1, column=0, padx=10, pady=10)
        self.label_email.grid(row=2, column=0, padx=10, pady=10)
        self.label_address.grid(row=3, column=0, padx=10, pady=10)

        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=10)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)
        self.entry_address.grid(row=3, column=1, padx=10, pady=10)

        self.button_add.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_view.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_search.grid(row=6, column=0, columnspan=2, pady=10)
        self.button_update.grid(row=7, column=0, columnspan=2, pady=10)
        self.button_delete.grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()

        if not name and not phone:
            messagebox.showerror("Error", "Enter either Name or Phone for searching.")
            return

        found_contacts = []
        for contact in self.contacts:
            if name and contact.get("Name") == name:
                found_contacts.append(contact)
            elif phone and contact.get("Phone") == phone:
                found_contacts.append(contact)

        if not found_contacts:
            messagebox.showinfo("Info", "No matching contacts found.")
        else:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in found_contacts])
            messagebox.showinfo("Matching Contacts", contact_list)

    def update_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()

        if not name or not phone:
            messagebox.showerror("Error", "Enter both Name and Phone to update a contact.")
            return

        for contact in self.contacts:
            if contact.get("Name") == name and contact.get("Phone") == phone:
                contact["Email"] = self.entry_email.get()
                contact["Address"] = self.entry_address.get()
                messagebox.showinfo("Success", "Contact updated successfully.")
                return

        messagebox.showinfo("Info", "No matching contact found for update.")

    def delete_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()

        if not name or not phone:
            messagebox.showerror("Error", "Enter both Name and Phone to delete a contact.")
            return

        for contact in self.contacts:
            if contact.get("Name") == name and contact.get("Phone") == phone:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully.")
                return

        messagebox.showinfo("Info", "No matching contact found for deletion.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()

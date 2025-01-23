import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("600x400")

        # Contact list
        self.contacts = []

        # Input fields
        self.name_label = tk.Label(self.root, text="Name:", font=("Arial", 12))
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(self.root, text="Phone:", font=("Arial", 12))
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry = tk.Entry(self.root, font=("Arial", 12))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(self.root, text="Email:", font=("Arial", 12))
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry = tk.Entry(self.root, font=("Arial", 12))
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(self.root, text="Address:", font=("Arial", 12))
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.address_entry = tk.Entry(self.root, font=("Arial", 12))
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact, font=("Arial", 12))
        self.add_button.grid(row=4, column=0, padx=10, pady=5)

        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts, font=("Arial", 12))
        self.view_button.grid(row=4, column=1, padx=10, pady=5)

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact, font=("Arial", 12))
        self.search_button.grid(row=5, column=0, padx=10, pady=5)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact, font=("Arial", 12))
        self.update_button.grid(row=5, column=1, padx=10, pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact, font=("Arial", 12))
        self.delete_button.grid(row=6, column=0, padx=10, pady=5)

        # Listbox for displaying contacts
        self.contact_listbox = tk.Listbox(self.root, font=("Arial", 12), width=50, height=10)
        self.contact_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone number are required!")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def search_contact(self):
        search_query = self.name_entry.get().strip()
        if search_query:
            self.contact_listbox.delete(0, tk.END)
            for contact in self.contacts:
                if search_query.lower() in contact['name'].lower() or search_query in contact['phone']:
                    self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
        else:
            messagebox.showerror("Error", "Please enter a name or phone number to search!")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            name = self.name_entry.get().strip()
            phone = self.phone_entry.get().strip()
            email = self.email_entry.get().strip()
            address = self.address_entry.get().strip()

            if name and phone:
                self.contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.view_contacts()
            else:
                messagebox.showerror("Error", "Name and phone number are required!")
        else:
            messagebox.showerror("Error", "No contact selected to update!")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.view_contacts()
        else:
            messagebox.showerror("Error", "No contact selected to delete!")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()

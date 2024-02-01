import tkinter as tk
from tkinter import *
from tkinter import messagebox as messagebox

# Define a class for the Doubly Linked List
class Node:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_contact(self, name, phone_number):
        new_contact = Node(name, phone_number)
        if not self.head:
            self.head = new_contact
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_contact
            new_contact.prev = current

    def delete_contact(self, name):
        current = self.head
        while current:
            if current.name == name:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return True
            current = current.next
        return False

# Create an instance of the DoublyLinkedList
contacts_list = DoublyLinkedList()

def add_contact():
    name = name_entry.get()
    phone_number = phone_number_entry.get()

    # Check if name and phone_number are not empty
    if name and phone_number:
        # Add the contact to the Doubly Linked List
        contacts_list.add_contact(name, phone_number)

        # Add the contact to the listbox
        contacts_listbox.insert(tk.END, f"{name}: {phone_number}")

        # Show a message box confirming the addition
        add_info = ("Name: " + name + "\nPhone Number: " + phone_number + "\nContact added successfully. ")
        messagebox.showinfo("Insert Result", add_info)
    else:
        # Show an error message if name or phone_number is empty
        messagebox.showerror("Insert Result", "Please provide both \nName \nand \nPhone Number.")

def delete_contact():
    selected_indices = contacts_listbox.curselection()

    # Check if an item is selected
    if selected_indices:
        selected_index = selected_indices[0]

        # Delete the contact from the listbox
        contacts_listbox.delete(selected_index)

        # Show a message box confirming the deletion
        messagebox.showinfo("Delete Result", "Contact deleted successfully.")

        # Delete the contact from the Doubly Linked List
        contact_info = contacts_listbox.get(selected_index)
        name = contact_info.split(":")[0].strip()
        if contacts_list.delete_contact(name):
            # Clear the input fields
            name_entry.delete(0, tk.END)
            phone_number_entry.delete(0, tk.END)
    else:
        # Show a message box indicating no contact selected for deletion
        messagebox.showerror("Delete Result", "No contact selected for deletion.")

def search_contact():
    name = name_entry.get()
    phone_number = phone_number_entry.get()

    if not name and not phone_number:
        # Show an error message if both name and phone_number are empty
        messagebox.showerror("Search Result", "Both Name and Phone Number are empty.")
        return

    # Search for the contact in the listbox using linear search
    contact_found = False

    for i, item in enumerate(contacts_listbox.get(0, tk.END)):
        item_name = item.split(":")[0].strip()
        if (name.lower() == item_name.lower() and name) and (phone_number == item.split(":")[1].strip() and phone_number):
            # Exact match found, select and scroll to the item
            # Clear the previous selection
            contacts_listbox.selection_clear(0, tk.END)
            contact_found = True
            contacts_listbox.select_set(i)
            contacts_listbox.see(i)
            messagebox.showinfo("Search Result","Exact contact found.")
            break

    # If no exact match, check for somewhat matching contacts
    if not contact_found:
        matching_contacts = []
        for i, item in enumerate(contacts_listbox.get(0, tk.END)):
            item_name = item.split(":")[0].strip()
            if (name.lower() == item_name.lower()) or (phone_number == item.split(":")[1].strip()):
                matching_contacts.append(item)

        if matching_contacts:
            # Somewhat matching contacts found, show them in a message box
            for contact in matching_contacts:
                contacts_listbox.select_set(i)
                contacts_listbox.see(i)
            messagebox.showinfo("Search Result", "Matching contacts found. ")
        else:
            # No matching contacts found
            messagebox.showerror("Search Result", "No contacts found.")

root = tk.Tk()
root.title("Phonebook Application")
root.geometry("400x550")
root.configure(bg="lightgray")

frame = Frame(root, bg="lightgray")
frame.pack()

title_label = Label(frame, text="Phonebook Application", anchor="center", font=("Arial", 18), height=3, fg="blue", bg="lightgray")
title_label.grid(row=0, column=0, columnspan=2)

name_label = Label(frame, text="Name:", font=("Arial", 13), height=2, bg="lightgray")
name_label.grid(row=1, column=0)
name_entry = Entry(frame)
name_entry.grid(row=1, column=1)

phone_number_label = Label(frame, text="Phone Number:", font=("Arial", 13), height=2, bg="lightgray")
phone_number_label.grid(row=2, column=0)
phone_number_entry = Entry(frame)
phone_number_entry.grid(row=2, column=1)

add_contact_button = Button(frame, text="Add Contact", command=add_contact, height=2, width=15, borderwidth=5)
add_contact_button.grid(row=3, column=0, columnspan=2, pady=10)  # Centered button with padding

search_contact_button = Button(frame, text="Search Contact", command=search_contact, height=2, width=15, borderwidth=5)
search_contact_button.grid(row=4, column=0, columnspan=2, pady=10)  # Centered button with padding

delete_contact_button = Button(frame, text="Delete Contact", command=delete_contact, height=2, width=15, borderwidth=5)
delete_contact_button.grid(row=5, column=0, columnspan=2, pady=10)  # Centered button with padding

contacts_listbox = Listbox(frame, width=40)
contacts_listbox.grid(row=6, column=0, columnspan=2)

root.mainloop()

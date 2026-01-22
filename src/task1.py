import sys
sys.stdout.reconfigure(encoding='utf-8') # type: ignore
import re


FILE_NAME = "contacts.txt"

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def is_valid_email(email):
        if "@" not in email:
         return False
        if not email.endswith(".com"):
         return False
        at_index = email.index("@")
        dot_index = email.rfind(".com")
        return at_index > 0 and at_index < dot_index


def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()
    company = input("Company: ").strip()
    birthday = input("Birthday (YYYY-MM-DD): ").strip()
    notes = input("Notes: ").strip()

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email},{address},{company},{birthday},{notes}\n")

    print("\n✅ Contact added successfully!\n")


def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        if not contacts:
            print("📭 No contacts found.\n")
            return

        print("\n📒 Contact List")
        print("=" * 60)

        for contact in contacts:
            name, phone, email, address, company, birthday, notes = contact.strip().split(",")

            print(f"""
Name     : {name}
Phone    : {phone}
Email    : {email}
Address  : {address}
Company  : {company}
Birthday : {birthday}
Notes    : {notes}
------------------------------
""")

    except FileNotFoundError:
        print("📭 No contacts file found.\n")


def search_contact():
    keyword = input("Search (name/phone/email/company): ").lower()
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for contact in file:
                fields = contact.strip().split(",")

                if any(keyword in field.lower() for field in fields):
                    name, phone, email, address, company, birthday, notes = fields

                    print(f"""
Contact Found
----------------
Name     : {name}
Phone    : {phone}
Email    : {email}
Address  : {address}
Company  : {company}
Birthday : {birthday}
Notes    : {notes}
""")
                    found = True

        if not found:
            print("❌ No matching contact found.\n")

    except FileNotFoundError:
        print("📭 No contacts file found.\n")


def main():
    while True:
        print("""
 Contact Book Menu
1. Add Contact
2. View Contacts
3. Search Contact
4. Exit
""")

        choice = input("Choose (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()

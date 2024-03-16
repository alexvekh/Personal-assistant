
def find_contacts(book, value):
    """
    Function to search for contacts by any field with a given value.

    Args:
        book: Dictionary with contacts.
        value: Value to search for.

    Returns:
        List of strings with information about found contacts.
    """

    found_contacts_info = []
    for record in book.values():
        contact_info = f"{record.name}:"
        if value.lower() in record.name.lower():
            contact_info += f"  Phones: {get_phones(record)}"
            contact_info += f"  Emails: {get_emails(record)}"
            contact_info += f"  Birthday: {record.birthday.value.strftime('%d.%m.%Y') if record.birthday else 'Not set'}"
            contact_info += f"  Note: {record.note if record.note else 'No note'}"
            found_contacts_info.append(contact_info)
        elif value in [phone.value for phone in record.phones]:
            contact_info += f"  Phones: {get_phones(record)}"
            contact_info += f"  Emails: {get_emails(record)}"
            contact_info += f"  Birthday: {record.birthday.value.strftime('%d.%m.%Y') if record.birthday else 'Not set'}"
            contact_info += f"  Note: {record.note if record.note else 'No note'}"
            found_contacts_info.append(contact_info)
        elif value in [email.value for email in record.emails]:
            contact_info += f"  Phones: {get_phones(record)}"
            contact_info += f"  Emails: {get_emails(record)}"
            contact_info += f"  Birthday: {record.birthday.value.strftime('%d.%m.%Y') if record.birthday else 'Not set'}"
            contact_info += f"  Note: {record.note if record.note else 'No note'}"
            found_contacts_info.append(contact_info)
        elif record.birthday and value == record.birthday.value.strftime("%d.%m.%Y"):
            contact_info += f"  Phones: {get_phones(record)}"
            contact_info += f"  Emails: {get_emails(record)}"
            contact_info += f"  Birthday: {record.birthday.value.strftime('%d.%m.%Y') if record.birthday else 'Not set'}"
            contact_info += f"  Note: {record.note if record.note else 'No note'}"
            found_contacts_info.append(contact_info)
        elif value in record.note:
            contact_info += f"  Phones: {get_phones(record)}"
            contact_info += f"  Emails: {get_emails(record)}"
            contact_info += f"  Birthday: {record.birthday.value.strftime('%d.%m.%Y') if record.birthday else 'Not set'}"
            contact_info += f"  Note: {record.note if record.note else 'No note'}"
            found_contacts_info.append(contact_info)

    return found_contacts_info

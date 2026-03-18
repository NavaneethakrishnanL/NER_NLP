import re

def extract_entities(text: str):

    entities = {}

    # Email
    email_pattern = r'\S+@\S+'
    email_match = re.findall(email_pattern, text)

    if email_match:
        return {
            "field": "email_id",
            "value": email_match[0]
        }

    # Phone
    phone_pattern = r'\b\d{10}\b'
    phone_match = re.findall(phone_pattern, text)

    if phone_match:
        return {
            "field": "phone",
            "value": phone_match[0]
        }

    # Name
    if "name" in text:
        value = text.split("name")[-1].strip()
        return {
            "field": "name",
            "value": value
        }

    # City
    if "city" in text:
        value = text.split("city")[-1].strip()
        return {
            "field": "city",
            "value": value
        }

    return None
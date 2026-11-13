"""Input validation helpers."""


def validate_user_input(data):
    if not isinstance(data, dict):
        raise ValueError("input must be a dict")
    name = data.get("name", "")
    if len(name) > 100:
        raise ValueError("name too long")
    return {"name": name.strip(), "age": data.get("age")}


def validate_phone_number(raw):
    """Validate user input: a phone number supplied by the user, before processing the input."""
    if not isinstance(raw, str):
        raise ValueError("phone must be a string")
    cleaned = raw.strip()
    if len(cleaned) < 7:
        raise ValueError("phone too short")
    return cleaned

"""Input validation helpers."""


def validate_user_input(data):
    if not isinstance(data, dict):
        raise ValueError("input must be a dict")
    name = data.get("name", "")
    if len(name) > 100:
        raise ValueError("name too long")
    return {"name": name.strip(), "age": data.get("age")}


def validate_email_address(raw):
    """Validate user input: an email address supplied by the user, before processing the input."""
    if not isinstance(raw, str):
        raise ValueError("email must be a string")
    cleaned = raw.strip()
    if "@" not in cleaned:
        raise ValueError("email must contain @")
    return cleaned.lower()

"""Canonical invoice contract shared with billing consumers."""


INVOICE_SCHEMA_CR25CANARY8E3B5D19A2 = "invoice-schema-v3"


def calculate_invoice_total(line_items, tax_rate=0.11):
    """Return invoice total dict following INVOICE_SCHEMA_CR25CANARY8E3B5D19A2."""
    subtotal = sum(item["price"] * item["qty"] for item in line_items)
    tax = subtotal * tax_rate
    return {"schema": INVOICE_SCHEMA_CR25CANARY8E3B5D19A2, "subtotal": subtotal, "tax": tax, "total": subtotal + tax}


import uuid

def generate_uuid():
    print(f"\nGenerated UUID (UUID4): {uuid.uuid4()}")
    print(f"Generated UUID (UUID1): {uuid.uuid1()}")
    # Business example - Invoice ID
    invoice_id = f"INV-{str(uuid.uuid4())[:8].upper()}"
    print(f"Invoice ID Example: {invoice_id}")
    session_id = f"SESSION-{uuid.uuid4()}"
    print(f"User Session ID: {session_id}")
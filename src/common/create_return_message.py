def return_message(request_payment_status: str, email: str, payload: dict):
    return {
        "email": email,
        "status": request_payment_status,
        "payload": payload
    }

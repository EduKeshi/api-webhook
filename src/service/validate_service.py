from src.enum import payment_status

from src.common.create_return_message import return_message
from src.repository.insert_data import create_collection
from src.repository.pymongo_get_database import get_database


def validate(request: dict):
    status = payment_status.payment_status()
    get_database()
    document = create_collection("attempts")

    message = return_message(request["status"], request["email"], request)

    document.insert_one(message.copy())

    if request["status"] == status["APPROVED"]:
        print(f"Liberar acesso do e-mail: {request['email']}")
        print(f"Enviar mensagem de boas vindas para o email: {request['email']}")

    elif request["status"] == status["REFUSED"]:
        print(f"Pagamento recusado para o e-mail: {request['email']}")

    elif request["status"] == status["REFUNDED"]:
        print(f"Acesso removido para o e-mail: {request['email']}")

    else:
        print("Status de pagamento inexistente.")

    return message

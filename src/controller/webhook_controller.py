from flask import Flask, request, Response
from flask import jsonify
from flask_jwt_extended import JWTManager, jwt_required

from src.service.attempts_service import attempts_service
from src.service.create_user_service import create_user_service
from src.service.login_user_service import login_user_service
from src.service.validate_service import validate

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "12343241321323"
jwt = JWTManager(app)


@app.route("/receive", methods=["POST"])
def receive_webhook():
    return validate(request.get_json())


@app.route("/user/create", methods=["POST"])
def create_user():
    create_user_service(request.get_json())

    return Response(status=201)


@app.route("/user/login", methods=["POST"])
def login_user():
    result = login_user_service(request.get_json())

    if result:
        return jsonify({
            "token": result
        })
    else:
        return Response(status=403)


@app.route("/attempts", methods=["GET"])
@jwt_required()
def attempts():
    result = attempts_service(request.args.get("email"))

    return result


if __name__ == "__main__":
    app.run(port=8085, host='0.0.0.0')

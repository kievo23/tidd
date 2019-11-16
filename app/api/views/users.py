from flask import Flask, Blueprint, request, make_response, jsonify
from app.api.models import users_model

USER = users_model.User()

user_route = Blueprint('user', __name__, url_prefix='/api/v1/user')

@user_route.route('', methods=['GET'])
def get_users():
    data = USER.get_users()
    return make_response(jsonify(data))

@user_route.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password']

    USER.register(email,password)

    return make_response(jsonify('success'))

@user_route.route('/login', methods=['POST'])
def login():
    data = request.get_users()
    email = data['email']
    password = data['password']

    USER.login(email, password)
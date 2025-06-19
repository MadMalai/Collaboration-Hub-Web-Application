from flask_restful import Resource
from flask import request, jsonify,make_response

from application.models import *
from application.models import db, user_datastore


class signup(Resource):
    def post(self):
        data = request.get_json()
        email1 = data.get('email')
        password1 = data.get('password')
        role1 = data.get('role')
        user = user_datastore.find_user(email=email1)
        if not user:
            user = user_datastore.create_user(email=email1, password=password1)
            if role1 == "sponsor":
                user_datastore.add_role_to_user(user, "sponsor")
                user_datastore.deactivate_user(user)
            elif role1 == "influencer":
                user_datastore.add_role_to_user(user, 'influencer')
            db.session.commit()
            return jsonify({"message":"User registered successfully","id":user.id})
        return jsonify({"message":"User already exists","id":user.id})

class login(Resource):
    def post(self):
        data = request.get_json()
        email1 = data.get('email')
        password1 = data.get('password')
        user = user_datastore.find_user(email=email1)
        if user:
            if user.active:
                roles = [role.name for role in user.roles][0]
                from flask_security.utils import verify_password
                if verify_password(password1, user.password):
                    return make_response(jsonify({"message":"Login successful", "authToken": user.get_auth_token(),"roles":roles,"user_id":user.id}), 201)
                else:
                    return make_response(jsonify({"message": "Invalid password"}), 401)
            else:
                return make_response(jsonify({"message": "Account is inactive. Please contact support."}), 403)
        else:
            return make_response(jsonify({"message": "Invalid email or user does not exist"}), 404)
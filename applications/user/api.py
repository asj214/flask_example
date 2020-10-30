from datetime import datetime
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from models import User
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import (
    create_access_token,
    jwt_optional,
    jwt_required,
    get_jwt_identity
)
from serializers import CreateUserSchema, LoginSchema, UserSchema


blueprint = Blueprint('api_user', __name__)

@blueprint.route('/api/users/login', methods=('POST',))
@jwt_optional
@use_kwargs(LoginSchema())
@marshal_with(LoginSchema())
def api_login(email, password):

    user = User.query.filter_by(email=email).one_or_none()

    if user is not None and check_password_hash(user.password, password):
        user.update(last_login_at=datetime.now())
        token = create_access_token(identity=user.id)
        return jsonify({'status': 200, 'access_token': token})

    return jsonify({'status': 404, 'message': 'not found your email'})


@blueprint.route('/api/users', methods=['POST'])
@jwt_optional
@use_kwargs(CreateUserSchema())
@marshal_with(UserSchema())
def create(email, name, password, **kwargs):

    if User.query.filter_by(email=email).one_or_none() is None:
        user = User(
            email=email,
            name=name,
            password=generate_password_hash(password)
        ).save()
        return user
    else:
        return jsonify({'status': 500, 'message': 'email has exists'})


@blueprint.route('/api/users', methods=['GET'])
@jwt_required
@marshal_with(UserSchema())
def show():

    id = get_jwt_identity()

    user = User.query.get(id)
    return user
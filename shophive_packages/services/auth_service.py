from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from shophive_packages.models.user import User
from shophive_packages import db

"""
This module contains the authentication services for user management,
including registration and login functionality.
"""


def register_user(username, email, password):
    """
    Registers a new user in the system.

    Args:
        username (str): The username of the new user.
        email (str): The email of the new user.
        password (str): The password of the new user.

    Returns:
        tuple: A dictionary message and an HTTP status code.
    """
    if User.query.filter_by(username=username).first():
        return {"message": "Username already exists."}, 400
    if User.query.filter_by(email=email).first():
        return {"message": "Email already exists."}, 400

    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return {"message": "User created successfully."}, 201


def authenticate_user(email, password):
    """
    Authenticates a user and generates a JWT token.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        tuple: A dictionary containing the access token and an HTTP status code,
               or an error message if authentication fails.
    """
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return {"message": "Invalid credentials."}, 401

    access_token = create_access_token(identity=user.id)
    return {"access_token": access_token}, 200

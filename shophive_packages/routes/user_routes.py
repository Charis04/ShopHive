from flask import Blueprint, request, jsonify
from shophive_packages.services.auth_service import register_user, authenticate_user

"""
This module defines the routes for user-related actions, such as registration
and login, and uses the authentication services.
"""

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/register', methods=['POST'])
def register():
    """
    Registers a new user by accepting JSON data with username, email, and password.

    Returns:
        JSON response with success or error message.
    """
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"message": "Missing fields"}), 400

    return jsonify(*register_user(username, email, password))


@user_routes.route('/login', methods=['POST'])
def login():
    """
    Authenticates a user and generates a JWT token.

    Returns:
        JSON response with access token or error message.
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Missing fields"}), 400

    return jsonify(*authenticate_user(email, password))


@user_routes.route('/users', methods=['GET'])
def get_users():
    """
    Fetches all registered users from the database.

    Returns:
        JSON response containing a list of all users (username and email).
    """
    from shophive_packages.models.user import User
    users = User.query.all()
    return jsonify([{'username': user.username, 'email': user.email} for user in users]), 200

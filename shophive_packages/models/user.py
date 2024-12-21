from shophive_packages import db

"""
This module defines the User model, representing users in the database.
"""


class User(db.Model):
    """
    Represents a user in the ShopHive platform.

    Attributes:
        id (int): Primary key for the user.
        username (str): Unique username for the user.
        email (str): Unique email for the user.
        password (str): Hashed password for the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the User object.
        """
        return f'<User {self.username}>'

from flask import Flask
from shophive_packages import db
from flask_migrate import Migrate
from shophive_packages.routes.user_routes import user_routes
import os

"""
This is the main application file for the ShopHive platform. It initializes
the Flask application, sets up configurations, and registers routes.
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)
migrate = Migrate(app, db)

# Register the blueprint for user routes
app.register_blueprint(user_routes)

# Debug registered tables
with app.app_context():
    from shophive_packages.models.user import User, Product
    print(f"Registered tables: {db.metadata.tables.keys()}")

if __name__ == '__main__':
    app.run(debug=True)

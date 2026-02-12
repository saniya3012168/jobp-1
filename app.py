from flask import Flask
from backend.config import Config
from backend.extensions import db, jwt, cors
from backend.routes import register_routes
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register blueprints
    register_routes(app)

    # Root route (to avoid 404 on "/")
    @app.route("/")
    def home():
        return {
            "status": "success",
            "message": "JobPilot API is running successfully 🚀"
        }

    # Create database tables
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)

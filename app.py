from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Import my_services to register the routes
from project.models.my_services import my_services_bp

# Register the Blueprint
app.register_blueprint(my_services_bp)

if __name__ == "__main__":
    app.run(port=5001, debug=True)  # You can specify the port here
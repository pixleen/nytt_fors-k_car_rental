from flask import Blueprint, jsonify, request
from project.models.my_dao import findAllCars, findCarByReg, save_car, update_car, delete_car

# Create a Blueprint
my_services_bp = Blueprint('my_services', __name__)

@my_services_bp.route('/get_cars', methods=['GET'])
def query_records():
    """Retrieve all cars."""
    try:
        cars = findAllCars()  # Call the DAO method to get all cars
        return jsonify(cars), 200  # Return the car data as JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle exceptions

@my_services_bp.route('/get_cars_by_reg_number', methods=['POST'])
def find_car_by_reg_number():
    """Find a car by its registration number."""
    record = request.get_json()  # Get JSON data from request
    reg_number = record.get('reg')  # Extract the registration number

    if not reg_number:
        return jsonify({"error": "Registration number is required"}), 400  # Bad request if no reg number is provided

    car = findCarByReg(reg_number)  # Call the DAO method to find the car
    if car:
        return jsonify(car), 200  # Return the found car data
    else:
        return jsonify({"error": "Car not found"}), 404  # Not found if car is not found

@my_services_bp.route('/save_car', methods=['POST'])
def save_car_info():
    """Save car information."""
    record = request.get_json()  # Get JSON data from request
    make = record.get('make')
    model = record.get('model')
    reg = record.get('reg')
    year = record.get('year')
    capacity = record.get('capacity')

    if not all([make, model, reg, year, capacity]):
        return jsonify({"error": "All fields are required"}), 400  # Bad request if any field is missing

    new_car = save_car(make, model, reg, year, capacity)  # Call the DAO method to save the car
    return jsonify(new_car), 201  # Return the saved car data

@my_services_bp.route('/update_car', methods=['PUT'])
def update_car_info():
    """Update car information."""
    record = request.get_json()  # Get JSON data from request
    reg = record.get('reg')

    if not reg:
        return jsonify({"error": "Registration number is required"}), 400  # Bad request if no reg number is provided

    updated_car = update_car(
        record.get('make'),
        record.get('model'),
        reg,
        record.get('year'),
        record.get('capacity')
    )  # Call the DAO method to update the car

    return jsonify(updated_car), 200  # Return the updated car data

@my_services_bp.route('/delete_car', methods=['DELETE'])
def delete_car_info():
    """Delete a car by its registration number."""
    record = request.get_json()  # Get JSON data from request
    reg = record.get('reg')

    if not reg:
        return jsonify({"error": "Registration number is required"}), 400  # Bad request if no reg number is provided

    delete_car(reg)  # Call the DAO method to delete the car
    return jsonify({"message": "Car deleted successfully"}), 204  # Return a success message
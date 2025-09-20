# app/routes/api_routes.py
from flask import Blueprint, jsonify
from .. import services

api_bp = Blueprint('api', __name__)

@api_bp.route('/data', methods=['GET'])
def get_data():
    """ An example API """
    data = {"howdy": "cowboy"}
    return jsonify(data)

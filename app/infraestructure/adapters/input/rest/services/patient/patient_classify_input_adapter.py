from app.infraestructure.adapters.input.rest.services.patient import blueprint
from flask import jsonify


@blueprint.route('/', methods=['GET'])
def classify():
    return jsonify({'status_code': 200, 'message': 'Classified'})

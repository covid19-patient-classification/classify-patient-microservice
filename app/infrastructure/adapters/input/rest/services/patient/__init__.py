from flask import Blueprint

blueprint = Blueprint(
    'patient_blueprint',
    __name__,
    url_prefix=''
)

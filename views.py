from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from models import SeveralParams
from werkzeug.exceptions import BadRequest

from query import main_query

bp_main = Blueprint("main", __name__)


@bp_main.route("/perform_query", methods=["POST"])
def perform_query():
    data = request.json
    # серилиазуем данные из запроса
    try:
        params = SeveralParams().load(data=data)
    except ValidationError as error:
        return jsonify(error.messages), 400
    result = None
    for i in params["qeuries"]:
        funk = main_query(cmd=i["cmd"], value=i["value"], res=result)
    return jsonify(funk)

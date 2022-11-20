from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from .models import SeveralParams
from typing import Iterable, Optional

from query import main_query

bp_main = Blueprint("main", __name__)


@bp_main.route("/perform_query", methods=["POST"])
def perform_query():
    # серилиазуем данные из запроса
    try:
        params = SeveralParams().load(data=request.json)
    except ValidationError as error:
        return jsonify(error.messages), 400

    result: Iterable[str] = None
    for i in params["qeuries"]:
        result = main_query(cmd=i["cmd"],
                            value=i["value"],
                            res=result)

    return jsonify(result)

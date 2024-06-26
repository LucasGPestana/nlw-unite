from flask import Blueprint, jsonify, request

from src.http_types.http_request import HttpRequest

from src.data.check_ins_handler import CheckInsHandler

from src.errors.error_handler import handle_error

check_ins_route_bp = Blueprint("check_ins_route", __name__)

@check_ins_route_bp.route("/attendees/<attendee_id>/check-in", methods=["POST"])
def create_ckeck_ins(attendee_id):

  try:

    check_ins_handler = CheckInsHandler()
    http_request = HttpRequest(params={"attendee_id": attendee_id})

    http_response = check_ins_handler.registry(http_request)

    return jsonify(http_response.body), http_response.status_code
  
  except Exception as exception:

        http_response = handle_error(exception)

        return jsonify(http_response.body), http_response.status_code
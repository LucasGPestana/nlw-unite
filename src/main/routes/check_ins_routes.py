from flask import Blueprint, jsonify, request

from src.http_types.http_request import HttpRequest

from src.data.check_ins_handler import CheckInsHandler

check_ins_route_bp = Blueprint("check_ins_route", __name__)

@check_ins_route_bp.route("/attendees/<attendee_id>/check-in", methods=["POST"])
def create_ckeck_ins(attendee_id):

  check_ins_handler = CheckInsHandler()
  http_request = HttpRequest(params={"attendee_id": attendee_id})

  http_response = check_ins_handler.registry(http_request)

  return jsonify(http_response.body), http_response.status_code
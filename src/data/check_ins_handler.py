from src.models.repository.check_ins_repository import CheckInsRepository

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class CheckInsHandler:

  def __init__(self) -> None:

    self.__check_ins_repository = CheckInsRepository()
  
  def registry(self, http_request: HttpRequest) -> HttpResponse:

    check_in_infos = http_request.params["attendee_id"]

    self.__check_ins_repository.insert_check_in(check_in_infos)

    return HttpResponse(
      body=None,
      status_code=201
    )


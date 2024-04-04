from src.models.entities.check_ins import CheckIns
from src.models.settings.connection import DB_CONNECTION_HANDLER

from sqlalchemy.exc import IntegrityError
from src.errors.error_types.http_conflict import HttpConflictError

class CheckInsRepository:

  def insert_check_in(self, attendee_id: str) -> str:

    with DB_CONNECTION_HANDLER as database:

      try:

        check_in = CheckIns(
          attendeeId=attendee_id
        )

        database.session.add(check_in)
        database.session.commit()

        return attendee_id
      
      except IntegrityError:

        raise HttpConflictError("Check-in já cadastrado!")
      
      except Exception as exception:

        database.session.rollback()
        raise exception
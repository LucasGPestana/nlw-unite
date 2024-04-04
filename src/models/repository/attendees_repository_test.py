from src.models.settings.connection import DB_CONNECTION_HANDLER
from .attendees_repository import AttendeesRepository
import pytest

DB_CONNECTION_HANDLER.connect_to_db()


@pytest.mark.skip(reason="Novo registro no banco de dados")
def test_insert_attendee():

    attendeeInfo = {
        "uuid": "meu_uuid_attendee",
        "name": "attendee_name",
        "email": "email@email.com",
        "event_id": "meu-uuid",
    }

    attendees_repository = AttendeesRepository()

    response = attendees_repository.insert_attendee(attendeeInfo)

    print(response)

@pytest.mark.skip(reason="Não necessita")
def test_get_attendee_badge_by_id():
    
    attendee_id = "meu_uuid_attendee"
    
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendee_badge_by_id(attendee_id)

    print(response.title)
    print(response.name)
    print(response.email)

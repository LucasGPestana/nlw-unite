from .events_repository import EventsRepository
from src.models.settings.connection import DB_CONNECTION_HANDLER
import pytest

DB_CONNECTION_HANDLER.connect_to_db()


@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_event():

    event = {
        "uuid": "meu-uuid2",
        "title": "titulo",
        "slug": "meu-slug-aqui2",
        "maximum_attendees": 20,
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)


#@pytest.mark.skip(reason="Não necessita")
def test_get_event_by_id():

    event_id = "meu-uuid123"

    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)

    print(response)
    #print(response.id)

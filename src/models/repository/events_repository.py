from typing import Dict
from src.models.settings.connection import DB_CONNECTION_HANDLER

from src.models.entities.events import Events
from src.models.entities.attendees import Attendees

from sqlalchemy.exc import IntegrityError, NoResultFound

from src.errors.error_types.http_conflict import HttpConflictError

class EventsRepository:

    def insert_event(self, eventsInfo: Dict) -> Dict:

        with DB_CONNECTION_HANDLER as database:

            try:
                event = Events(
                    id=eventsInfo.get("uuid"),
                    title=eventsInfo.get("title"),
                    details=eventsInfo.get("details"),
                    slug=eventsInfo.get("slug"),
                    maximum_attendees=eventsInfo.get("maximum_attendees")
                )

                database.session.add(event)
                database.session.commit()

                return eventsInfo

            except IntegrityError:

                raise HttpConflictError("Evento já cadastrado!")

            except Exception as exception:

                database.session.rollback()
                raise exception

    def get_event_by_id(self, event_id: str) -> Events:

        with DB_CONNECTION_HANDLER as database:

            try:

                event = database.session.query(Events).filter(
                    Events.id == event_id).one()

                return event

            except NoResultFound:

                return None

    def count_event_attendees(self, event_id: str) -> Dict:

        with DB_CONNECTION_HANDLER as database:


            event_count = (
                database.session
                .query(Events)
                .join(Attendees, Events.id == Attendees.event_id)
                .filter(Events.id == event_id)
                .with_entities(
                    Events.maximum_attendees,
                    Attendees.id
                )
                .all()
            )

            if not len(event_count):
                return {
                    "maximumAttendees": 0,
                    "attendeesAmount": 0,
                }
                
            return {
                    "maximumAttendees": event_count[0].maximum_attendees,
                    "attendeesAmount": len(event_count),
                }

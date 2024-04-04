from typing import Dict, List

from src.models.settings.connection import DB_CONNECTION_HANDLER

from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from src.models.entities.check_ins import CheckIns

from sqlalchemy.engine.row import Row
from sqlalchemy.exc import IntegrityError, NoResultFound


class AttendeesRepository:

    def insert_attendee(self, attendeeInfo: Dict) -> Dict:

        with DB_CONNECTION_HANDLER as database:

            try:

                attendee = Attendees(
                    id=attendeeInfo.get("uuid"),
                    name=attendeeInfo.get("name"),
                    email=attendeeInfo.get("email"),
                    event_id=attendeeInfo.get("event_id")
                )

                database.session.add(attendee)
                database.session.commit()

                return attendeeInfo

            except IntegrityError:

                raise Exception("Participante já cadastrado!")

            except Exception as exception:

                database.session.rollback()
                raise exception

    def get_attendee_badge_by_id(self, attendee_id: str) -> Row:

        with DB_CONNECTION_HANDLER as database:

            try:

                attendee = (
                    database.session
                    .query(Attendees)
                    .join(Events, Events.id == Attendees.event_id)
                    .filter(Attendees.id == attendee_id)
                    .with_entities(
                        Attendees.name,
                        Attendees.email,
                        Events.title
                    )
                    .one()
                )

                return attendee

            except NoResultFound:

                return None

    def get_attendees_by_event_id(self, event_id: str) -> List[Row]:

        with DB_CONNECTION_HANDLER as database:

            attendees = (
                database.session
                .query(Attendees)
                .outerjoin(CheckIns, CheckIns.attendeeId == Attendees.id)
                .filter(Attendees.event_id == event_id)
                .with_entities(
                    Attendees.id,
                    Attendees.name,
                    Attendees.email,
                    CheckIns.created_at.label("checkedInAt"),
                    Attendees.created_at.label("createdAt")
                ).all()
            )

            return attendees

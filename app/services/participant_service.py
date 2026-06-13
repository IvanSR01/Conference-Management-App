from fastapi import HTTPException
from starlette import status

from sqlalchemy.orm import Session

from app.models import Participant
from app.schemas.participant import ParticipantCreate, ParticipantUpdate


class ParticipantService:
    """
    Сервис работы с участниками.
    """

    @staticmethod
    def get_all(db: Session):
        """
        Получение всех участников.
        """

        return (
            db.query(Participant)
            .order_by(Participant.id.desc())
            .all()
        )

    @staticmethod
    def create(
            db: Session,
            participant_data: ParticipantCreate
    ):
        """
        Создание участника.
        """

        # Проверяем, зарегистрирован ли уже участник
        # на данную конференцию
        duplicate = (
            db.query(Participant)
            .filter(
                Participant.email == participant_data.email,
                Participant.conference_name == participant_data.conference_name
            )
            .first()
        )

        if duplicate:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "Участник уже зарегистрирован "
                    "на данную конференцию."
                )
            )

        participant = Participant(
            full_name=participant_data.full_name,
            email=participant_data.email,
            organization=participant_data.organization,
            conference_name=participant_data.conference_name
        )

        db.add(participant)

        db.commit()

        db.refresh(participant)

        return participant

    @staticmethod
    def update(
            db: Session,
            participant_id: int,
            participant_data: ParticipantUpdate
    ):
        """
        Обновление участника.
        """

        participant = (
            db.query(Participant)
            .filter(
                Participant.id == participant_id
            )
            .first()
        )

        if not participant:
            return None

        duplicate = (
            db.query(Participant)
            .filter(
                Participant.email ==
                participant_data.email,

                Participant.conference_name ==
                participant_data.conference_name,

                Participant.id != participant_id
            )
            .first()
        )

        if duplicate:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Участник уже зарегистрирован на данную конференцию."
            )

        participant.full_name = participant_data.full_name
        participant.email = participant_data.email
        participant.organization = participant_data.organization
        participant.conference_name = participant_data.conference_name

        db.commit()

        db.refresh(participant)

        return participant

    @staticmethod
    def delete(
            db: Session,
            participant_id: int
    ):
        """
        Удаление участника.
        """

        participant = (
            db.query(Participant)
            .filter(
                Participant.id == participant_id
            )
            .first()
        )

        if not participant:
            return False

        db.delete(participant)

        db.commit()

        return True
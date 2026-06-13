from sqlalchemy import Column, Integer, String

from app.database import Base


class Participant(Base):
    """
    Модель участника конференции.
    Соответствует таблице participants.
    """

    __tablename__ = "participants"

    # Уникальный идентификатор участника
    id = Column(Integer, primary_key=True, index=True)

    # ФИО участника
    full_name = Column(String, nullable=False)

    # Электронная почта
    email = Column(String, nullable=False)

    # Организация участника
    organization = Column(String, nullable=False)

    # Название конференции
    conference_name = Column(String, nullable=False)
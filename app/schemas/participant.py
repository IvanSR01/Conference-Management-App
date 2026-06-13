from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field


class ParticipantBase(BaseModel):
    """
    Базовая схема участника.
    """

    full_name: str = Field(
        min_length=5,
        max_length=100
    )

    email: EmailStr

    organization: str = Field(
        min_length=2,
        max_length=100
    )

    conference_name: str = Field(
        min_length=2,
        max_length=100
    )


class ParticipantCreate(ParticipantBase):
    """
    Схема создания.
    """
    pass


class ParticipantUpdate(ParticipantBase):
    """
    Схема обновления.
    """
    pass


class ParticipantResponse(ParticipantBase):
    """
    Схема ответа.
    """

    id: int

    model_config = ConfigDict(
        from_attributes=True
    )
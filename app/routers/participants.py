from fastapi import APIRouter
from fastapi import Depends
from fastapi import Form
from fastapi import Request

from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
from starlette import status

from app.database import get_db
from app.schemas.participant import ParticipantCreate, ParticipantUpdate
from app.services.participant_service import ParticipantService

# Роутер участников
router = APIRouter(
    tags=["Participants"]
)

# Подключаем шаблоны
templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/")
def get_participants(
        request: Request,
        db: Session = Depends(get_db)
):
    """
    Главная страница со списком участников.
    """

    participants = ParticipantService.get_all(db)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "participants": participants
        }
    )

@router.post(
    "/participants",
    status_code=status.HTTP_201_CREATED
)
def create_participant(
    participant_data: ParticipantCreate,
    db: Session = Depends(get_db)
):
    """
    Создание нового участника.
    """

    participant = ParticipantService.create(
        db=db,
        participant_data=participant_data
    )

    return participant

@router.put(
    "/participants/{participant_id}"
)
def update_participant(
        participant_id: int,

        participant_data: ParticipantUpdate,

        db: Session = Depends(get_db)
):
    """
    Обновление участника.
    """

    ParticipantService.update(
        db=db,
        participant_id=participant_id,
        participant_data=participant_data
    )

    return RedirectResponse(
        url="/",
        status_code=303
    )


@router.delete("/participants/{participant_id}")
def delete_participant(
        participant_id: int,
        db: Session = Depends(get_db)
):
    """
    Удаление участника.
    """

    success = ParticipantService.delete(
        db=db,
        participant_id=participant_id
    )

    return {
        "success": success
    }

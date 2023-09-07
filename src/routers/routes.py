from fastapi import APIRouter
from services.text_translate import generate_text
from schema.Doc import Doc


router = APIRouter()


@router.get("/")
def start():
    return "hello world"

@router.post("/translater")
def response(request: Doc):

    message = request.sentence

    result = generate_text(message)
    return result
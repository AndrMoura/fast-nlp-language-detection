import logging

from typing import Dict, List, Union
from fastapi import APIRouter
from pydantic import BaseModel
from src.language_detect import get_task_user_agent_languages
from rest_api.schema import TaskInput


logger = logging.getLogger(__name__)
router = APIRouter()


class Request(BaseModel):
    texts: Union[str, List[str]]


@router.post(
    "/conversation_language_detect_plugin",
    response_model=Dict[str, Union[List[str], int]],
)
async def task_language_detect(request: TaskInput):
    return get_task_user_agent_languages(request.llm_input, request.llm_output)

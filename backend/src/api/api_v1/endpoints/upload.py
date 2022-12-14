from typing import Any

from fastapi import APIRouter, Depends, File, UploadFile

from src import models, schemas
from src.api import deps
from src.utils.files import host_file

router = APIRouter()


@router.post(
    "/uploadfile/",
    response_model=schemas.Msg,
)
def upload(
    *,
    file: UploadFile = File(...),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Upload a file, return an url that has access to it
    """
    url = host_file(file)
    return {"result": url}

from typing import Dict, Union, List, Annotated

from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.project.dao import ProjectDAO
from app.project.schemas import SProject, SProjects

router = APIRouter(
    prefix="/projects",
    tags=["Проекты"]
)


@router.get("")
@cache(expire=20)
async def get_projects(page: Annotated[int, Query(gt=0)] = 1, limit: Annotated[int, Query(gt=0)] = 5) -> Dict[str, Union[str, List[SProjects]]]:
    projects = await ProjectDAO.get_all()


    return {"detail": "Все записи", "result": projects[page - 1:limit]}


@router.get("/{project_id}")
@cache(expire=20)
async def get_project(project_id: int) -> Dict[str, Union[str, SProject]]:
    print("QWEEWQQ 1")
    project = await ProjectDAO.find_by_id(project_id)
    print("QWEEWQQ")
    if not project:
        return JSONResponse({"detail": "Проект не найден!"}, status_code=status.HTTP_404_NOT_FOUND)

    return {"detail": "Все записи", "result": project}



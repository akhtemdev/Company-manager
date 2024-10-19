from typing import Optional

from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.api.utils.auth_protect import admin_required
from src.models.user import User
from src.services.structure import StructureService
from src.shemas.structure_router import (
    AssignManagerResponse,
    DepartmentResponse,
    MessageResponse,
    PositionResponse,
)

router = APIRouter(
    prefix='/structure',
    tags=['Structure']
)


@router.post('/departments/', status_code=HTTP_201_CREATED)
async def create_department(
    name: str,
    parent_id: Optional[int] = None,
    current_user: User = Depends(admin_required),
    service: StructureService = Depends(StructureService)
) -> DepartmentResponse:
    return await service.create_department(name, parent_id, current_user)


@router.post('/positions/', status_code=HTTP_201_CREATED)
async def create_position(
    name: str,
    department_id: int,
    current_user: User = Depends(admin_required),
    service: StructureService = Depends(StructureService)
) -> PositionResponse:
    return await service.create_position(name, department_id, current_user)


@router.post('/assign-position/', status_code=HTTP_200_OK)
async def assign_position_to_user(
    user_id: int,
    position_id: int,
    current_user: User = Depends(admin_required),
    service: StructureService = Depends(StructureService)
) -> MessageResponse:
    return await service.assign_position_to_user(
        user_id, position_id, current_user
    )


@router.post(
        '/departments/{department_id}/assign-manager/',
        status_code=HTTP_200_OK
)
async def assign_manager(
    department_id: int,
    user_id: int,
    current_user: User = Depends(admin_required),
    service: StructureService = Depends(StructureService)
) -> AssignManagerResponse:
    return await service.assign_manager(department_id, user_id, current_user)


@router.delete('/departments/delete/', status_code=HTTP_204_NO_CONTENT)
async def delete_department(
    department_id: int,
    current_user: User = Depends(admin_required),
    service: StructureService = Depends(StructureService)
) -> MessageResponse:
    return await service.delete_department(department_id, current_user)

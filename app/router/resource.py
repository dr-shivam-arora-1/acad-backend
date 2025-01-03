from fastapi import APIRouter
from app.config.constant import RESOURCE_ENTITY_TAG
router = APIRouter(tags=[RESOURCE_ENTITY_TAG])


@router.get("")
def get_resource():
    return "gets resource"

@router.post("")
def post_resource():
    return "posts resource"


@router.put("")
def put_resource():
    return "puts resource"

@router.delete("")
def delete_resource():
    return "deletes resource"
from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, utils, bible,\
    bible_chapter, bible_verse, organization, organization_user

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(
    organization.router, prefix="/organization", tags=["organization"])
api_router.include_router(
    organization_user.router, prefix="/organization-user", tags=["organization-user"])
api_router.include_router(bible.router, prefix="/bible", tags=["bible"])
api_router.include_router(bible_chapter.router,
                          prefix="/bible-chapter", tags=["bible-chapter"])
api_router.include_router(
    bible_verse.router, prefix="/bible-verse", tags=["bible-verse"])

api_router.include_router(utils.router, prefix="/utils", tags=["utils"])

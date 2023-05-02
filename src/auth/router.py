from fastapi import APIRouter, Depends

from auth.dependencies import auth_redirect_or_login, auth_redirect_or_authentication, logout
from auth.services.authentication import AuthenticationService
from auth.services.login import LoginService
from auth.services.logout import LogoutService

router = APIRouter()


@router.get(path="/login")
async def login(login_service: LoginService = Depends(auth_redirect_or_login)):
    return login_service.result()


@router.post(path="/login")
async def login(auth_service: AuthenticationService = Depends(auth_redirect_or_authentication)):
    return auth_service.result()


@router.get("/logout")
async def logout(logout_service: LogoutService = Depends(logout)):
    return logout_service.result()

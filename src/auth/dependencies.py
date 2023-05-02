from fastapi import Depends

from auth.services.app_auth import ApplicationAuthRedirectService
from auth.services.authentication import AuthenticationService
from auth.services.client import ClientApplicationConfig
from auth.services.login import LoginService
from auth.services.logout import LogoutService
from auth.utils import check_token


def auth_redirect_or_login(
        login_service: LoginService = Depends(),
        redirect_service: ApplicationAuthRedirectService = Depends(),
        token_exists: bool = Depends(check_token)
):
    if token_exists:
        return redirect_service
    else:
        return login_service


def auth_redirect_or_authentication(
        redirect_service: ApplicationAuthRedirectService = Depends(),
        auth_service: AuthenticationService = Depends(),
        token_exists: bool = Depends(check_token)
):
    if token_exists:
        return redirect_service
    else:
        return auth_service


def logout(logout_service: LogoutService = Depends()):
    return logout_service


def get_client(client: ClientApplicationConfig = Depends()):
    return client

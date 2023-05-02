from starlette.responses import RedirectResponse

from auth.services.base import ApplicationService


class LogoutService(ApplicationService):
    def result(self):
        response = RedirectResponse("/login")
        response.delete_cookie(key="sso_auth")
        return response

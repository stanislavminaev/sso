from typing import Optional, List, Dict

from fastapi import Form, Depends
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from auth.services.base import ApplicationService
from auth.utils import create_token, check_login_error


class AuthenticationService(ApplicationService):

    def __init__(
            self,
            request: Request,
            username: Optional[str] = Form(None),
            password: Optional[str] = Form(None),
            errors: List = Depends(check_login_error),
            jwt: str = Depends(create_token)
    ):
        self.request = request
        self.username = username
        self.password = password
        self.errors = errors
        self.jwt = jwt
        self.templates = Jinja2Templates(directory="templates")

    @property
    def context(self) -> Dict:
        return {"request": self.request, "username": self.username, "password": self.password, "errors": self.errors}

    def result(self):
        if self.errors:
            return self.templates.TemplateResponse("login.html", self.context)
        response = RedirectResponse(f"/login")
        response.set_cookie(key="sso_auth", value=self.jwt)
        return response

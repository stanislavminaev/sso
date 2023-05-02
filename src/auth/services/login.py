from typing import Dict

from starlette.requests import Request
from starlette.templating import Jinja2Templates

from auth.services.base import ApplicationService


class LoginService(ApplicationService):
    """
    Класс авторизации пользователя
    """
    def __init__(self, request: Request):
        self.request = request
        self.templates = Jinja2Templates(directory="templates")

    @property
    def context(self) -> Dict:
        return {"request": self.request}

    def result(self):
        return self.templates.TemplateResponse("login.html", self.context)


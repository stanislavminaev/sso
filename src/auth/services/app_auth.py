from fastapi import Depends
from starlette.responses import RedirectResponse
from jwt import encode

from auth.services.base import ApplicationService
from auth.services.client import ClientApplicationConfig
from auth.utils import check_token


class ApplicationAuthRedirectService(ApplicationService):
    def __init__(self, username: str = Depends(check_token), client: ClientApplicationConfig = Depends()):
        self.client_url = client.url
        self.client_jwt = encode({"username": username}, client.key, algorithm="HS256")

    def result(self):
        url = f"{self.client_url}?jwt={self.client_jwt}"
        return RedirectResponse(url=url)

data = {
    "dev": {
        "url": "https://localhost:12200/auth",
        "key": "secret"
    }
}


class ClientApplicationConfig:

    def __init__(self, guid: str = ""):
        global data
        self.url = data.get(guid, dict()).get("url", "/")
        self.key = data.get(guid, dict()).get("key", "")

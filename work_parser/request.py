from requests import Response
import requests
from fake_useragent import UserAgent

class RequestEngine:
    def get_response(self, url: str, params: dict | None = None) -> Response:
        user_agent = UserAgent()
        response = requests.get(url, params=params, headers={"User-Agent": user_agent.random})
        return response  # Повернення відповіді

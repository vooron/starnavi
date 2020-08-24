import base64
import json
from datetime import datetime
from typing import Tuple

import requests

ApiClientResponse = Tuple[int, dict]


class APIClient:
    _api_base_path: str
    _access_token: str
    _refresh_token: str
    _expires: datetime

    def __init__(self, api_base_path: str, access_token: str = None, refresh_token: str = None):
        self._validate_path(api_base_path)
        self._api_base_path = api_base_path
        self._access_token = access_token
        self._refresh_token = refresh_token
        if access_token:
            self._update_token_info()

    def _validate_path(self, path: str):
        if path[-1] != '/':
            raise ValueError(f"Path '{path}' should ends with '/'.")

    def get(self, path: str) -> ApiClientResponse:
        self._validate_path(path)
        headers = {
            'Content-Type': 'application/json',
        }
        if self._access_token:
            self._refresh_token_if_needed()
            headers['Authorization'] = 'Bearer ' + self._access_token

        resp = requests.get(self._api_base_path + path, headers=headers)
        return resp.status_code, resp.json()

    def post(self, path: str, data: dict) -> ApiClientResponse:
        self._validate_path(path)
        headers = {
            'Content-Type': 'application/json',
        }
        if self._access_token:
            self._refresh_token_if_needed()
            headers['Authorization'] = 'Bearer ' + self._access_token
        resp = requests.post(self._api_base_path + path, headers=headers, data=json.dumps(data))
        return resp.status_code, resp.json()

    def signup(self, username, email, password) -> ApiClientResponse:
        return self.post('auth/registration/', {"username": username, "email": email, "password": password})

    def login(self, username, password) -> 'APIClient':
        code, data = self.post("auth/login/", {"username": username, "password": password})
        return APIClient(self._api_base_path, data['access'], data['refresh'])

    def _add_padding_to_token_if_needed(self, b64_string):
        return b64_string + "=" * ((4 - len(b64_string) % 4) % 4)

    def _update_token_info(self):
        b64_string = self._add_padding_to_token_if_needed(self._access_token.split('.')[1])
        token_decoded = json.loads(base64.b64decode(b64_string))
        self._expires = datetime.fromtimestamp(token_decoded['exp'])

    def _refresh_token_if_needed(self):
        if datetime.now() >= self._expires:
            self.refresh_token()

    def refresh_token(self) -> None:
        code, data = self.post('auth/refresh/', {"refresh": self._refresh_token})
        self._access_token = data['access']
        self._refresh_token = data['refresh']
        self._update_token_info()

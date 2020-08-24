from abc import ABCMeta, abstractmethod, ABC

from _bot.services import APIClient
from _bot.utils import get_random_string


class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, request: dict) -> dict:
        pass


class ServerManipulationCommand(Command, ABC):
    _api_client: APIClient

    def __init__(self, api_client: APIClient):
        self._api_client = api_client


class CreateRandomUserCommand(ServerManipulationCommand):
    USERNAME_LENGTH: int = 10
    PASSWORD_LENGTH: int = 10
    USERNAME_PREFIX: str = "random_user"
    EMAIL_DOMAIN: str = 'google.com'
    EMAIL_LENGTH: int = 5

    def _generate_random_user_credentials(self) -> dict:
        return {
            "email": get_random_string(self.EMAIL_LENGTH) + "@" + self.EMAIL_DOMAIN,
            "username": self.USERNAME_PREFIX + get_random_string(self.USERNAME_LENGTH),
            "password": get_random_string(self.PASSWORD_LENGTH)
        }

    def execute(self, request: dict) -> dict:
        credentials = self._generate_random_user_credentials()
        code, data = self._api_client.signup(**credentials)
        if code != 201:
            raise Exception(f"User was not created. Answer code {code} and response {data}")
        return {"credentials": credentials}


class SignInUserCommand(ServerManipulationCommand):

    def execute(self, request: dict) -> dict:
        credentials = request['credentials']
        authenticated_api_client = self._api_client.login(
            username=credentials['username'], password=credentials['password'])

        return {
            "user": {
                **credentials,
                "authenticated_api_client": authenticated_api_client
            }
        }


class CreateRandomPostCommand(Command):
    TITLE_LENGTH: int = 10
    CONTENT_LENGTH: int = 10

    TARGET_PATH: str = 'posts/'

    def _get_random_post_data(self) -> dict:
        return {
            "title": get_random_string(self.TITLE_LENGTH),
            "content": get_random_string(self.CONTENT_LENGTH)
        }

    def execute(self, request: dict) -> dict:
        api_client: APIClient = request['user']['authenticated_api_client']
        code, data = api_client.post(self.TARGET_PATH, self._get_random_post_data())
        if code != 201:
            raise Exception(f"Post was not created. Answer code {code} and response {data}")
        return {
            "post": data,
            "author": request['user']
        }


class LikePostCommand(Command):
    TARGET_PATH: str = 'posts/{}/likes/'

    def execute(self, request: dict) -> dict:
        api_client: APIClient = request['user']['authenticated_api_client']
        code, data = api_client.post(self.TARGET_PATH.format(request['post']['id']), {})
        if code != 201:
            raise Exception(f"Post was not Liked. Answer code {code} and response {data}")
        return {}

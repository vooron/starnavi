import json

from _bot.bot_strategy import BotStrategy
from _bot.commands import (CreateRandomUserCommand,
                           SignInUserCommand, CreateRandomPostCommand, LikePostCommand)
from _bot.services import APIClient


def main():
    unauthenticated_api_client = APIClient('http://localhost:8000/api/')

    strategy = BotStrategy(
        CreateRandomUserCommand(unauthenticated_api_client),
        SignInUserCommand(unauthenticated_api_client),
        CreateRandomPostCommand(),
        LikePostCommand()
    )

    with open('configurations.json') as f:
        strategy.process(json.load(f))

    # client = unauthenticated_api_client.login() // enter your username and password to check
    # result = client.get("analytics/")
    # print(result)


if __name__ == "__main__":
    main()

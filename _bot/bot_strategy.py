from random import randrange, sample
from typing import List

from _bot.commands import (Command)


class BotStrategy:
    _create_user: Command = None
    _sing_in_user: Command = None
    _create_post: Command = None
    _like_post: Command = None

    def __init__(
            self,
            create_user: Command,
            sing_in_user: Command,
            create_post: Command,
            like_post: Command
    ):
        self._create_user = create_user
        self._sing_in_user = sing_in_user
        self._create_post = create_post
        self._like_post = like_post

    def _create_n_posts(self, login_user_result: dict, number_of_posts: int) -> List[dict]:
        post_creation_results = []
        for i in range(number_of_posts):
            post_creation_results.append(self._create_post.execute(login_user_result))
        return post_creation_results

    def _like_n_random_posts(self, sign_in_user_result: dict, post_creation_results: list, number_posts: int):
        for post_creation_result in sample(post_creation_results, number_posts):
            post_creation_result['user'] = sign_in_user_result['user']
            self._like_post.execute(post_creation_result)

    def process(self, configuration: dict):
        post_creation_results = []
        sign_in_user_results = []

        for i in range(configuration['number_of_users']):
            create_user_result = self._create_user.execute({})
            sign_in_user_result = self._sing_in_user.execute(create_user_result)
            sign_in_user_results.append(sign_in_user_result)

            post_creation_results.extend(
                self._create_n_posts(
                    sign_in_user_result,
                    randrange(0, configuration['number_of_users'] + 1)
                )
            )

        for sign_in_user_result in sign_in_user_results:
            self._like_n_random_posts(
                sign_in_user_result, post_creation_results, randrange(0, configuration['max_likes_per_user']))

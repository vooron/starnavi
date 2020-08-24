import random
import string


def get_random_string(length: int) -> str:
    return "".join([random.choice(string.ascii_letters)
                    for x in range(length)])

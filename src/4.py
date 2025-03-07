
import random

def get_random_code():
    code = "".join([chr(random.randint(97, 122)) for _ in range(8)])
    return code
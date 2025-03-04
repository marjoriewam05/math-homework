import random

def get_random_code():
  """Returns a random string of letters and numbers"""
  return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(10))

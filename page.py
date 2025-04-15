import string
import random

letters = string.ascii_lowercase
randomlettersinrange = ''.join(random.choice(letters) for _ in range(12))

print(randomlettersinrange)

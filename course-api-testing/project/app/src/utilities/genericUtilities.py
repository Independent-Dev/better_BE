import logging as logger
import random
import string


def generatte_email_and_pw(domain=None, email_prefix=None):
    logger.debug('Generating random email and pw')

    if not domain:
        domain = 'mystore.local'
    if not email_prefix:
        email_prefix = 'test_user'

    random_email_str_len = 10
    random_str_email = ''.join(random.choices(
        string.ascii_lowercase, k=random_email_str_len))

    email = email_prefix + "_" + random_str_email + "@" + domain

    pw_len = 20
    password = ''.join(random.choices(string.ascii_lowercase, k=pw_len))

    random_info = {'email': email, "password": password}
    logger.debug(f"email and pw: {random_info}")

    return random_info

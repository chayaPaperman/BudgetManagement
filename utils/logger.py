import functools
import logging
from fastapi import Request, Response

logging.basicConfig(filename='utils/server.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def log_request(func):
    """
    A decorator that logs to a file for each server call
    """

    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs['request']
        method = request.method
        path = request.url.path
        logging.info(f"{request.client.host}: {method} {path} ")
        response: Response = await func(*args, **kwargs)
        return response

    return wrapper

import functools
import logging
from fastapi import  Request,Response

logging.basicConfig(filename='utils/server.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def log_request(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs['request']  # Assuming the request object is the second argument
        method = request.method
        path = request.url.path
        logging.info(f"{request.client.host}: {method} {path} ")
        response: Response = await func(*args, **kwargs)
        return response
    return wrapper

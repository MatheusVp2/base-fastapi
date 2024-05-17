from fastapi.exceptions import HTTPException

__all__ = ['HTTPExceptionUnauthorized', 'HTTPExceptionForbidden']


class HTTPExceptionUnauthorized(HTTPException):
    def __init__(self):
        super().__init__(status_code=401)


class HTTPExceptionForbidden(HTTPException):
    def __init__(self):
        super().__init__(status_code=403)

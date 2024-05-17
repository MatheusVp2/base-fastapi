from pydantic import BaseModel

__all__ = ['User']


class User(BaseModel):
    username: str
    password: str

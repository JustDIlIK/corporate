from fastapi import HTTPException, status

class BaseExceptions(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class EntryCannotBeAdd(BaseExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Не получается добавить в базу"


class UserAlreadyExistsException(BaseExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Такой пользователь уже существует"


class EmailAlreadyExistsException(BaseExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Данная почта уже была использована"


class IncorrectEmailOrPasswordException(BaseExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный логин или пароль"


class TokenExpiredException(BaseExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен истек"


class TokenAbsentException(BaseExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токент отсутствует"


class IncorrectTokenFormatException(BaseExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"


class InvalidURLException(BaseExceptions):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Неверный формат url"
from typing import Any


class EventEmailGeneralException(Exception):
    message = "Unexpected error occurred."
    error_code = "EVENT_EMAIL_GENERAL_EXCEPTION"

    def __str__(self):
        return self.message


class EntityAlreadyExistsException(EventEmailGeneralException):
    error_code = 'ENTITY_ALREADY_EXISTS'

    def __init__(self, entity: str, entity_id: Any, entity_id_name: str = 'id'):
        self.message = f'{entity.capitalize()} with {entity_id_name} {entity_id} is already exists.'

    def __str__(self):
        return self.message


class LoginFailException(Exception):
    message = "Login fail."
    error_code = "LOGIN_FAIL_EXCEPTION"

    def __str__(self):
        return self.message


class InvalidTokenError(EventEmailGeneralException):
    error_code = 'INVALID_TOKEN_ERROR'


class ExpiredTokenError(EventEmailGeneralException):
    error_code = 'EXPIRED_TOKEN_ERROR'


class FailResponse(Exception):
    status_code: int = 400
    error_code: str = 'FAIL_RESPONSE'

    def __init__(self, message, status_code=None, payload=None, error_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        if error_code is not None:
            self.error_code = error_code
        self.payload = payload

    def to_dict(self):
        return {'errorCode': self.error_code, 'message': self.message, 'payload': self.payload}

    def __str__(self):
        return self.message

def ResponseModel(data, message) -> dict:
    return {
        "data": [data],
        "code": 200,
        "message": message
    }


def ErrorResponseModel(error, code, message) -> dict:
    return {
        "error": error,
        "code": code,
        "message": message
    }
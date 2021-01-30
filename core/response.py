from rest_framework import status
from rest_framework.response import Response


def exception_response(e):
    return Response(
        {
            'status': 403,
            'error': e.__str__()
        },
        status=status.HTTP_403_FORBIDDEN
    )


def success_message(message="", data=''):
    return Response(
        {
            'status': 200,
            'message': message,
            'data': data
        },
        status=status.HTTP_200_OK
    )

from rest_framework.exceptions import APIException


class NotConnected(APIException):
    status_code = 403
    default_detail = "you cannot connect to this person!"

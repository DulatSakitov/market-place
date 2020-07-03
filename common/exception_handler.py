from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == 401:
            if context:
                request = context.get('request')
                if request is not None:
                    ch = request.META.get('HTTP_CUSTOM401')
                    if ch:
                        try:
                            value = int(ch)
                        except ValueError:
                            pass
                        else:
                            if 399 < value < 500:
                                response.status_code = value

    return response

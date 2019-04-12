from django.core.signals import got_request_exception


def buggyview(request):
    raise ValueError("Original error with valuable error message")


def handler(signal, sender, **kwargs):
    # The handler is buggy, too
    raise KeyError("Django hurt itself in confusion")


got_request_exception.connect(handler)

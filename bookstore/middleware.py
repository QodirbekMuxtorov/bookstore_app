import time


class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.perf_counter()

        response = self.get_response(request)

        duration = (time.perf_counter() - start) * 1000
        print(f"[MIDDLEWARE] {request.method} {request.path} — {duration:.2f} ms")

        return response
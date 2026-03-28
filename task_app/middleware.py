# This middleware will just print the request method and path and the time it took to process the request

import time


class RequestLoggingMiddleware:
    def __init__(self, get_response):

        ## get_response is a function that is supposed to contain the logic of getting response for this request
        self.get_response = get_response

    def __call__(self, request):
        # Before time
        start_time = time.time()
        print(f"Request Started: {request.method} {request.path}")

        # Call View
        response = self.get_response(request)

        # After View
        end_time = time.time()
        duration = end_time - start_time
        print(
            f"Request Completed: {request.method} {request.path} in {duration:.4f} seconds"
        )
        return response

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(["GET"])
def add(request: Request):
    n1 = int(request.GET.get("num1"))
    n2 = int(request.GET.get("num2"))

    return Response({"n1": n1, "n2": n2, "result": n1 + n2})


@api_view(["GET"])
def sub(request: Request):
    n1 = int(request.GET.get("num1"))
    n2 = int(request.GET.get("num2"))

    return Response({"num1": n1, "num2": n2, "result": n1 - n2})


@api_view(["GET"])
def multiply(request: Request):
    n1 = int(request.GET.get("num1"))
    n2 = int(request.GET.get("num2"))
    return Response({"num1": n1, "num2": n2, "result": n1 * n2})


@api_view(["GET"])
def div(request: Request):
    n1 = int(request.GET.get("num1"))
    n2 = int(request.GET.get("num2"))
    return Response({"num1": n1, "num2": n2, "result": n1 / n2})

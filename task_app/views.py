from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer


@api_view(["GET"])
def index(request: Request):
    return Response(
        {
            "message": "Welcome to the Task Management API",
            "endpoints": {
                "tasks": {
                    "add": "/task/add/",
                    "list": "/task/get/",
                    "details": "/task/get/<id>/",
                },
                "users": {
                    "add": "/user/add/",
                    "list": "/user/get/",
                    "details": "/user/get/<id>/",
                },
                "jobs": {
                    "/jobs/",
                },
                "admin": "/admin/",
            },
        }
    )


@api_view(["POST"])
def add_task(request: Request):
    user_id = request.data.get("user_id")
    if user_id is None:
        return Response({"error": "user_id is required"}, status=400)

    try:
        user_id = int(user_id)
    except (TypeError, ValueError):
        return Response({"error": "user_id must be an integer"}, status=400)

    if not User.objects.filter(id=user_id).exists():
        return Response({"error": "user not found"}, status=404)

    serializer = TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    task = serializer.save()
    return Response(TaskSerializer(task).data, status=201)


@api_view(["POST"])
def add_user(request: Request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = User.objects.create(**serializer.validated_data)
    return Response(UserSerializer(user).data, status=201)


@api_view(["POST"])
def create_user(request: Request):
    return add_user(request)


@api_view(["GET"])
def get_users(request: Request):
    users = User.objects.all().order_by("id")
    return Response(UserSerializer(users, many=True).data)


@api_view(["GET"])
def get_user_by_id(request: Request, user_id: int):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "user not found"}, status=404)

    return Response(UserSerializer(user).data)


## Write an API to read all tasks for a given user_id


@api_view(["GET"])
def get_tasks(request: Request):
    user_id_param = request.query_params.get("user_id") or request.query_params.get(
        "id"
    )

    if not user_id_param:
        return Response({"error": "user_id is required"}, status=400)

    try:
        user_id = int(user_id_param)
    except ValueError:
        return Response({"error": "user_id must be an integer"}, status=400)

    tasks = Task.objects.filter(user_id=user_id)
    return Response(TaskSerializer(tasks, many=True).data)


@api_view(["GET"])
def get_task_by_id(request: Request, task_id: int):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({"error": "task not found"}, status=404)

    return Response(TaskSerializer(task).data)

from rest_framework import viewsets
from .models import Application
from .serializers import ApplicationSerializer


"""
=============================================================================
INITIAL VERSION: Function Based Views (FBVs)
=============================================================================
This was where we started. Separate functions for every action.
Hard to maintain as the project grows!

@api_view(["POST"])
def create_application(request):
    serializer = ApplicationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)

@api_view(["GET"])
def get_all_applications(request):
    applications = Application.objects.all()
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data, status=200)
    
@api_view(["GET"])
def get_application_by_id(request, pk):
    application = Application.objects.get(pk=pk)
    serializer = ApplicationSerializer(application)
    return Response(serializer.data, status=200)
"""

"""
=============================================================================
PREVIOUS EVOLUTION: ViewSet (Standard Implementation)
=============================================================================
In this phase, we moved from functions to a class. We had to manually 
define list(), create(), and retrieve() methods.

class ApplicationViewSet(viewsets.ViewSet):
    def list(self, request):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=200)

    def create(self, request):
        serializer = ApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None):
        try:
            application = Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            return Response({"error": "Not found"}, status=404)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data, status=200)
"""


# =============================================================================
# FINAL EVOLUTION: ModelViewSet (Current Active Code)
# =============================================================================
# This is the most efficient way to handle CRUD. DRF handles all logic
# (GET, POST, PUT, DELETE) automatically using the queryset and serializer.
class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        # Only return records that are NOT soft-deleted
        return Application.objects.filter(is_deleted=False)

    def perform_destroy(self, instance):
        # Soft delete: mark as deleted instead of removing from DB
        instance.is_deleted = True
        instance.save()

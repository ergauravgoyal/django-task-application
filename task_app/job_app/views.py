from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Job
from .serializers import JobSerializer
from rest_framework.viewsets import ViewSet


class JobViewSet(ViewSet):

    ## We just have to override the methods of the ViewSet class
    def list(self, request: Request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def create(self, request: Request):
        serializer = JobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    # Retrieving the specific job id
    def retrieve(self, request: Request, pk=None):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "job not found"}, status=404)
        serializer = JobSerializer(job)
        return Response(serializer.data)

    # Updating the specific job id
    def update(self, request: Request, pk=None):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "job not found"}, status=404)
        serializer = JobSerializer(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request: Request, pk=None):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "job not found"}, status=404)
        serializer = JobSerializer(job, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request: Request, pk=None):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "job not found"}, status=404)
        job.delete()
        return Response(status=204)


# class JobViewSet(ModelViewSet):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer

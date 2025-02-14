from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from Core.models import Record
import json
from datetime import datetime


class RegisterLocalBaseUpdate(APIView):
    def post(self, request):
        try:
            request_json = json.loads(request.body.decode())
        except ValueError:
            return Response({
                "status": "error",
                "error": "Incorrect Data"
            })
        observer_record = Record(timestamp=request_json['timestamp'], status='created', change=request_json['changes'], author='local')
        observer_record.save()
        return Response({
            "status": "Good"
        })
    def get(self, request):
        return Response({
            "status": "error",
            "error": "Only POST request"
        })
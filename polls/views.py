from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import permissions, viewsets

from .models import Question
from .serializers import QuestionSerializer


def index(request):
    return HttpResponse("WAGTAIL POC. Hello, world. You're at the polls index.")


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

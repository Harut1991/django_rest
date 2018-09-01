from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthenticatedAndAdmin
from .serializer import TestSerializer, QuestionSerializer, AnswerSerializer, UserAnswerSerializer
from .models import Test, Question, Answer, UserAnswer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticatedAndAdmin]
    http_method_names = ["get", "post", "delete"]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedAndAdmin]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('test',)
    search_fields = ('quesion_text',)
    http_method_names = ["get", "post", "delete"]


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticatedAndAdmin]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('question',)
    http_method_names = ["get", "post", "delete"]


class UserAnswerViewSet(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user',)
    http_method_names = ["get", "post", "delete"]

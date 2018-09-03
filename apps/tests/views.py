from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .filter import  ActorFilter
from .permissions import IsAuthenticatedAndAdmin
from .serializer import TestSerializer, QuestionSerializer, AnswerSerializer, UserAnswerSerializer, UserImageSerializer
from .models import Test, Question, Answer, UserAnswer, UserPhoto


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
    filter_class = ActorFilter
    http_method_names = ["get", "post", "delete"]


class UserAnswerViewSet(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user',)
    http_method_names = ["get", "post", "delete"]

class UserImageViewSet(APIView):
    serializer_class = UserImageSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        get_data = request.query_params
        user_query = get_data.get('user', False)

        if user_query:
            user = User.objects.filter(id=int(user_query)).first()
            if not user:
                return Response({'error': 'User dose not exist'}, status=status.HTTP_404_NOT_FOUND)
            exit(user.username)
            userfile = UserPhoto.objects.filter(user_id=user.id)
        else:
            userfile = UserPhoto.objects.all()

        serializer = self.serializer_class(userfile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            userFile = UserPhoto(
                image=serializer.validated_data['image'],
                user=request.user
            )
            userFile.save()
            return Response({'result': 'success'}, status=status.HTTP_200_OK)

        if serializer.errors:
            error = {
                "error": serializer.errors['image'][0]
            }

        return Response(error, status=status.HTTP_400_BAD_REQUEST)
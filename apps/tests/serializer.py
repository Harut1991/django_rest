from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Test, Question, Answer, UserAnswer


class TestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    test_questions = serializers.ReadOnlyField(source='get_test_questions')

    class Meta:
        model = Test
        fields = (
            'id',
            'name',
            'test_questions'
        )


class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    question_text = serializers.CharField(max_length=200)
    test = serializers.PrimaryKeyRelatedField(
        queryset=Test.objects.all(),
        required=True,
        allow_empty=False
    )
    test_detail = serializers.ReadOnlyField(source="get_test_detail")
    question_answers = serializers.ReadOnlyField(source='get_question_answers')

    class Meta:
        model = Question
        fields = (
            'id',
            'question_text',
            'test_detail',
            'question_answers',
            'test'
        )


class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    answer_text = serializers.CharField(max_length=200)
    correct_answer = serializers.BooleanField(default=False)
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all(),
        required=True,
        allow_empty=False
    )

    question_detail = serializers.ReadOnlyField(source='get_question_details')

    class Meta:
        model = Answer
        fields = (
            'id',
            'answer_text',
            'question',
            'question_detail',
            'correct_answer'
        )


class UserAnswerSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True,
        allow_empty=False
    )
    answer = serializers.PrimaryKeyRelatedField(
        queryset=Answer.objects.all(),
        required=True,
        allow_empty=False
    )

    answer_detail = serializers.ReadOnlyField(source='get_answer_detail')

    class Meta:
        model = UserAnswer
        fields = (
            'id',
            'user',
            'answer',
            'answer_detail'
        )

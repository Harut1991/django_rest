
from django.contrib.auth.models import User
from django.db import models

from .upload_path import get_image_path


class Test(models.Model):
    name = models.CharField(max_length=200)

    @property
    def get_test_questions(self):
        questions = Question.objects.filter(test=self)
        return_data = []
        if questions:
            for i in questions:
                return_data.append({'id': i.id, 'question_text': i.question_text})
        return return_data

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Test'


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    @property
    def get_question_answers(self):
        answers = Answer.objects.filter(question=self)
        return_data = []
        if answers:
            for i in answers:
                return_data.append({'id': i.id, 'answer_text': i.answer_text, 'correct_answer': i.correct_answer})
        return return_data

    @property
    def get_test_detail(self):
        return {'id': self.test.id, 'name': self.test.name}

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name_plural = 'Question'


class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct_answer = models.BooleanField(default=False)

    @property
    def get_question_details(self):
        return {'id': self.question.id, 'question_text': self.question.question_text,
                'test': {
                    'id': self.question.test.id,
                    'name': self.question.test.name
                }}

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name_plural = 'Answer'


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    @property
    def get_answer_detail(self):
        return {'id': self.answer.id, 'answer_text': self.answer.answer_text,
                'correct_answer': self.answer.correct_answer}

    def __str__(self):
        return self.answer.answer_text

    class Meta:
        verbose_name_plural = 'UserAnswer'

class UserPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=get_image_path,
        null=False,
    )

    def __str__(self):
        return self.image

    class Meta:
        verbose_name_plural= 'UserPhoto'

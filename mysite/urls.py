"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from apps.tests.views import TestViewSet, QuestionViewSet, AnswerViewSet, UserAnswerViewSet, UserImageViewSet
from apps.user.views import LoginViewSet, CreateUserView

schema_view = get_swagger_view(title='New API')
router = routers.SimpleRouter()
router.register(r'^tests', TestViewSet)
router.register(r'^questions', QuestionViewSet)
router.register(r'^answers', AnswerViewSet)
router.register(r'^user-answers', UserAnswerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^sign-in', LoginViewSet.as_view()),
    url(r'^user-photo', UserImageViewSet.as_view()),
    url(r'^sign-up', CreateUserView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

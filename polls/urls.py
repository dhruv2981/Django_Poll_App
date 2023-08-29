from django.urls import path
from . import views

app_name="polls"
urlpatterns = [
    path("",views.index,name='index'),
    path("results/<int:question_id>/",views.results,name='results'),
    path("<int:question_id>/",views.detail,name='detail'),
    path("vote/<int:question_id>/",views.vote,name='vote')
]


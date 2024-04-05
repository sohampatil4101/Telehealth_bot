from . import views
from django.urls import path


urlpatterns = [
    path('ask',views.Ask.as_view()),

]

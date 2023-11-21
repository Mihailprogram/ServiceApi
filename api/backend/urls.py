# urls.py
from django.urls import path

from backend.views import History, TestServer, Ping, Query, Result

urlpatterns = [
    path('v1/history', History.as_view()),
    path('v1/testserver', TestServer.as_view()),
    path('v1/ping', Ping.as_view()),
    path('v1/query', Query.as_view()),
    path('v1/result/<int:id>/', Result.as_view()),

]
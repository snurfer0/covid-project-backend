from django.urls import path, include
from django.contrib import admin
from .views import (
    apiOverview,
    UserList,
    UserDetail,
    TestList,
    TestDetail,
)

urlpatterns = [
    path('', apiOverview),
    path('admin/', include('rest_framework.urls')),
    path('auth/', admin.site.urls),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('tests/', TestList.as_view()),
    path('tests/<int:pk>/', TestDetail.as_view()),
]

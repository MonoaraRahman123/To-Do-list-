from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from students.api_views import StudentViewSet
from tasks.api_views import TaskViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student-api')
router.register(r'tasks', TaskViewSet, basename='task-api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login'), name='root'),
    path('accounts/', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('tasks/', include('tasks.urls')),
    path('api/', include(router.urls)),
]

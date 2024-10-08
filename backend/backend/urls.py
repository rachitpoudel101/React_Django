from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin routes
    path('api/', include(router.urls)),  # API routes

    # React frontend
    path('', views.serve_react),

]

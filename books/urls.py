from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login_view, name='login'),

]

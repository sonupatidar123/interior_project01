from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import contact_view
from .views import create_admin_once


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

# project/urls.py
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', views.current_user, name='current_user'),  # fetch logged-in user
    path('messages/', contact_view, name='contact'),
    path('setup-admin-secretly/', create_admin_once),
]


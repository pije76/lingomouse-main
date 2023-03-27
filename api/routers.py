from django.urls import path, re_path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

from dj_rest_auth.registration.views import SocialAccountListView, SocialAccountDisconnectView

from .views import *

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course')
router.register('levels', LevelViewSet, basename='level')

urlpatterns = [
	path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    path("auth/google/", GoogleLogin.as_view(), name="google_login"),
    path('socialaccounts/', SocialAccountListView.as_view(), name='social_account_list'),
    path('socialaccounts/<int:pk>/disconnect/', SocialAccountDisconnectView.as_view(), name='social_account_disconnect'),
]

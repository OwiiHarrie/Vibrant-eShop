from django.urls import path, re_path
from .views import (
    CustomProviderAuthView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    CustomTokenObtainPairView,
    LogoutView
)

urlpatterns = [
    re_path(
        r'^o/(?P<provider>\S+)/$',
        CustomProviderAuthView.as_view(),
        name='provider-auth'
    ),
    path('jwt/create/', CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('jwt/logout/', LogoutView.as_view()),
]

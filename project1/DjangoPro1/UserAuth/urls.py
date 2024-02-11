from django.urls import path
from .views import register_user, login_user,logout_user

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', register_user, name='register-user'),
    path('login/', login_user, name='login-user'),
    path('logout/', logout_user, name='logout-user'),
]
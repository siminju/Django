from django.urls import path
from .views import Users, MyInfo, Login, Logout, JWTLogin, UserDetailView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView

)

urlpatterns = [
    path("", Users.as_view()),
    path("myinfo", MyInfo.as_view()),


    path("getToken", obtain_auth_token),
    path("login", Login.as_view()),
    path("logout", Logout.as_view()),

    path("login/jwt", JWTLogin.as_view()),
    path("login/jwt/info", UserDetailView.as_view()),

    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refesh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view())
]

#{
#    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MTYxNTcxNSwiaWF0IjoxNzUxNTI5MzE1LCJqdGkiOiJlNTUxZjIwMTcyMTY0ZWMyODE4MWRjMmM1ZDgxNWFkMyIsInVzZXJfaWQiOjR9.SETO4kFvA486tbu1dEAZG_e40qov-V4R7QQti7KKNLM",
#    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUxNTMyOTE1LCJpYXQiOjE3NTE1MjkzMTUsImp0aSI6IjgyNWRjMDcwZjQ2YzQ5NTRiN2M4NGZmODE1YWRjYTk2IiwidXNlcl9pZCI6NH0.9lnLt9YKVEkzN6cGTJz9uhIOLIS8HWzxBINyebyBhCE"
#}
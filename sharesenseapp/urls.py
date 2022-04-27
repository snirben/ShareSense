from django.urls import path
from sharesenseapp.views import MyObtainTokenPairView,RegisterView,usersListApiView,sendEmail
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/users', usersListApiView.as_view()),
    path('api/email', sendEmail)
]
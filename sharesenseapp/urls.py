from django.urls import path
from sharesenseapp.views import MyObtainTokenPairView, RegisterView, togglePanic, usersListApiView, sendEmail, \
    whoIsInAPanicApiView,fireCamsListApiView, toggleFire
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/users/', usersListApiView.as_view()),
    path('api/email/', sendEmail),
    path('api/panic/', whoIsInAPanicApiView.as_view()),
    path('api/togglePanic/', togglePanic),
    path('api/toggleFire/', toggleFire),
    path('api/getcams/', fireCamsListApiView.as_view()),

]

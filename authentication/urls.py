from django.urls import path, include
from .views import GoogleLogin
app_name = 'authentication'


urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('social/login/google/', GoogleLogin.as_view(), name='google_login'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name="signup"),
    path('oauth2/', views.oauth, name='oauth2'),
    path('oauth2/redirect/', views.oauth_redir, name='oauth-redir'),
    path('oauth2/step-2/', views.oauth_step2, name='oauth-step2'),
    path('oauth2/step-3', views.oauth_step3, name='oauth_step3')
]
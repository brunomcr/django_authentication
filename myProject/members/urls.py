from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "members"
urlpatterns = [
    # Django Authentication URLS
    path("sign_in/", views.sign_in, name="sign_in"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("sign_out/", views.sign_out, name="sign_out"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

from django.urls import path
from apps.accounts import views
from django.contrib.auth.decorators import login_required

app_name = "accounts"
urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/',login_required(views.user_registration), name="register"),
    path('change-password/', login_required(views.change_password), name="cambiar_contrasena"),
]
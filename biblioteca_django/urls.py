
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from .views import HomeView, LoginView, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),

    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from .views import HomeView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
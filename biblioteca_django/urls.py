
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from .views import HomeView, LoginView, RegisterView, logout_view
from Library.views import BookDetailView, BookCreateView, AuthorCreateView, AuthorDetailView, AuthorAutocomplete


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),

    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),

    path("book-detail/<pk>", BookDetailView.as_view(), name="book-detail" ),
    path("book-create/", BookCreateView.as_view(), name="book-create"),

    path("author-create/", AuthorCreateView.as_view(), name="author-create"),
    path("author-detail/<pk>", AuthorDetailView.as_view(), name="author-detail"),
    path('author-autocomplete/', AuthorAutocomplete.as_view(), name='author-autocomplete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
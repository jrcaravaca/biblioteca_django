
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from .views import HomeView, LoginView, RegisterView, LoanHistoryView,logout_view, acces_denied
from Library.views import ( BookDetailView, BookCreateView, AuthorCreateView, AuthorDetailView, 
                        AuthorAutocomplete, BookListView, AuthorListView, BookDeleteView,
                        AuthorDeleteView, BookUpdateView, AuthorUpdateView)

from Users.views import UserProfileDetailView, UserProfileUpdateView




urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),

    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("loan-history/", LoanHistoryView.as_view(), name="loan-history"),

    path("book-detail/<pk>", BookDetailView.as_view(), name="book-detail" ),
    path("book-create/", BookCreateView.as_view(), name="book-create"),
    path("book-list/", BookListView.as_view(), name="book-list"),
    path("book-delete/<pk>", BookDeleteView.as_view(), name="book-delete"),
    path("book-update/<pk>", BookUpdateView.as_view(), name="book-update"),

    path("author-create/", AuthorCreateView.as_view(), name="author-create"),
    path("author-detail/<pk>", AuthorDetailView.as_view(), name="author-detail"),
    path('author-autocomplete/', AuthorAutocomplete.as_view(), name='author-autocomplete'),
    path("author-delete/<pk>", AuthorDeleteView.as_view(), name="author-delete"),
    path("author-list/", AuthorListView.as_view(), name="author-list"),
    path("author-update/<pk>", AuthorUpdateView.as_view(), name="author-update"),

    path("user-profile/<pk>", UserProfileDetailView.as_view(), name="user-profile"),
    path("user-profile-update/<pk>", UserProfileUpdateView.as_view(), name="user-profile-update"),

    path("access-denied/", acces_denied, name="access-denied")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
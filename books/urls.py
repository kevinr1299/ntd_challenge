from rest_framework.routers import DefaultRouter

from books.views import BookLikedViewSet

app_name = "books"

books_router = DefaultRouter()
books_router.register(r"liked_books", BookLikedViewSet, basename="api-liked-books")

urlpatterns = books_router.urls

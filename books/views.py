from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from books.models import Book
from books.serializers import BookSerializer


@extend_schema(tags=["Books"])
class BookLikedViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Goodreads is a social media platform for books.
    Users use it to keep track of their favorite books` and
    network with friends to discover new books. Given a user,
    could you find all the books in their social network?


    For Python:
    You’re building a simplified version of Goodreads using Django.
    Task:
    Implement an API endpoint that, given a user’s ID, returns all books liked by the user and everyone in their extended social network (i.e., their friends, friends of friends, etc.).
    Requirements:
    Define appropriate models: User, Book, and Friendship.

    Use Django’s ORM to retrieve the books.

    Create a view that returns a JSON response with the list of book titles.

    Avoid duplicates.
    """  # noqa: E501

    queryset = Book.objects.none()
    serializer_class = BookSerializer
    # TODO: Change to use token authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.liked_by_user_and_network(self.request.user)

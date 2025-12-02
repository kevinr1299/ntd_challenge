from django.urls import include, path

app_name = "ntd_challenge"


urlpatterns = [
    path("planets/", include("planets.urls", namespace="planets")),
    path("books/", include("books.urls", namespace="books")),
]

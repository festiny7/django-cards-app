from django.urls import path

from .views import (
    CardListView,
    BoxView,
    CardCreateView,
    CardUpdateView,
)


urlpatterns = [
    path("", CardListView.as_view(), name="card-list"),
    path("box/<int:box_num>",BoxView.as_view(), name="box"),
    path("new/",CardCreateView.as_view(), name="card-create"),
    path("card/edit/<int:pk>",CardUpdateView.as_view(), name="card-update"),
]
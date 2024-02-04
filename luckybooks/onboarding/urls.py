from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup1, name="signup1"),
    path("signup/nickname=<nickname>", views.signup2, name="signup2"),
    path("signup/bookselect/nickname=<nickname>%gender=<gender>%age=<age>", views.bookselect, name="bookselect"),
    path("genreselect", views.genreselect, name="genreselect"),
    path("authorselect", views.authorselect, name="authorselect"),
    path("underselection", views.underselection, name="underselection"),
]
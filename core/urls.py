from django.urls import path
from django.views import View
from . import views
from .views import News_feed_list, PeopleSearch, ProfileUpdate, ProfileView, post_detail, CommentDeleteView, PostDeleteView, PasswordUpdate, AddFollower
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [ 
    path("", views.index, name = "index"),
    path("login/", views.login, name = "login"),
    path("Register/", views.Register, name = "Register"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path("AboutUs/", views.AboutUs, name = "AboutUs"),
    path("FAQ/", views.FAQ, name = "FAQ"),
    path("login/", views.login, name = "login"), 
    path("logout/", views.logout_view, name = "logout"), 
    path("feed/", News_feed_list.as_view(), name="feed"),
    path("like/<int:pk>", views.like_post, name = "like_post"),
    path("post_detail/<int:pk>", post_detail.as_view(), name = "post_detail"), 
    path("comment_delete/<int:pk>", CommentDeleteView.as_view(), name = "comment_delete"),
    path("<int:pk>/profile/", ProfileView.as_view(), name= "profile"),   
    path("<int:pk>/profile_update/", ProfileUpdate.as_view(), name= "profile_update"), 
    path("<int:pk>/password_update/",PasswordUpdate.as_view(), name= "password_update"),
    path("password_success/",views.passsword_success, name= "password_success"),
    path("<int:pk>/post_delete/", PostDeleteView.as_view(), name= "post_delete"),
    path("<int:pk>/profile/add_follower", AddFollower.as_view(), name= "add_follower"),
    path("people_search/", PeopleSearch.as_view(), name = "people_search"),
]
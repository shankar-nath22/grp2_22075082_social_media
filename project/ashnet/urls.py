
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('login',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('register',views.register,name="register"),
    path("saved", views.saved, name="saved"),
    path("following", views.following, name='following'),
    path("search/<str:pagetype>", views.search, name='search'),
    path("editprofilebegin/<str:username>",views.editprofilebegin, name="editprofilebegin"),
    path("editprofile",views.editprofile, name="editprofile"),
     path("deleteprofilebegin",views.deleteprofilebegin, name="deleteprofilebegin"),
    path("deleteprofile",views.deleteprofile, name="deleteprofile"),
    path("createpost", views.create_post, name="createpost"),
    path("post/<int:id>/like", views.like_post, name="likepost"),
    path("post/<int:id>/unlike", views.unlike_post, name="unlikepost"),
    path("post/<int:id>/save", views.save_post, name="savepost"),
    path("post/<int:id>/unsave", views.unsave_post, name="unsavepost"),
    path("post/<int:post_id>/comments", views.comment, name="comments"),
    path("post/<int:post_id>/write_comment",views.comment, name="writecomment"),
    path("post/<int:post_id>/delete", views.delete_post, name="deletepost"),
    path("post/<int:post_id>/edit", views.edit_post, name="editpost"),
    path("<str:username>/follow", views.follow, name="followuser"),
    path("<str:username>/unfollow", views.unfollow, name="unfollowuser"),
    path("<str:username>", views.profile, name='profile')
    
]



from django.urls import path
from . import views

from .views import Homeview,ArticleDetailView,Categoryview,CategoryListView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,LikeView,AddCommentView,BlogView,AboutView,ContactView


# urlpatterns = [
#     path('',views.home,name='home'),
#     path('blogpost',views.blogpost,name='blogpost'),
# ]

urlpatterns = [
    path('',Homeview.as_view(), name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(), name='article-detail'),
    path('add_post', AddPostView.as_view(), name='add_post'),
    path('add_category', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>', Categoryview.as_view(), name='category'),
    path('category_list', CategoryListView.as_view(), name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('about-us',AboutView.as_view(),name='about'),
    path('blog',BlogView.as_view(),name='blog'),
    path('contact-us',ContactView.as_view(),name='contact_us'),
]

# remember to slugify categories links
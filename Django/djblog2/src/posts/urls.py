from django.urls import path
from posts.views import post_list,post_detail,new_post,edit_post,delete_post






app_name='posts'

urlpatterns = [
     
    path('',post_list,name='post_list'),
    path('new',new_post,name='post_new'),
    path('<int:id>' ,post_detail,name='post_detail'),
    path('<int:id>/edit' ,edit_post,name='post_edit'),
    path('<int:id>/delete' ,delete_post,name='post_delete'),
]

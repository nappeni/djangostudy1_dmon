from django.urls import path
from . import views
app_name = 'blog1'  # URL Reverse에서 namespace 기능을 한다.
urlpatterns = [
    path('',views.post_list, name='post_list'),
]
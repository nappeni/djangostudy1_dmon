from django.urls import path, re_path, register_converter

from . import views


class YearConverter:
    regex = r'20\d{2}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value


register_converter(YearConverter, 'year')

app_name = 'instagram'  # URL Reverse에서 namespace 기능을 한다.

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('<int:pk>/', views.post_detail, name="post_detail"),
    path('archives/<year:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>\d{4})/', views.archives_year),
    # re_path(r'(?P<pk>\d+)/$', views/post_detail)
]

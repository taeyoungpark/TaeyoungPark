
from django.conf.urls import url


urlpatterns = [
    url(r'^$','blog.views.index'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail', name='post_detail'),
    url(r'^(?P<pk>\d+)/edit$', 'blog.views.post_edit', name='post_edit'),

]

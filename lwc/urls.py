from django.urls import re_path
from django.contrib import admin

# from joins import views as joins_views
from joins.views import home as home_view, share as share_view

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', home_view, name='home'),
    #url(r'^testhome$', 'lwc.views.testhome', name='testhome'),
    re_path(r'^(?P<ref_id>.*)$', share_view, name='share'),
    # Examples:
    #url(r'^home2/$', 'lwc.views.home2', name='home'),
    # url(r'^blog/', include('blog.urls')),
]

from django.conf.urls import patterns, include, url
from bookraves_user.views import Login
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookraves.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Login.as_view(), name='login'),
)

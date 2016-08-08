from django.conf.urls import include, url
from django.contrib import admin
from protocol.views import sachin
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sachin$', sachin, name='sachin'),
]
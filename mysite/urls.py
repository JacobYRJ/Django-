from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import current_datetime
from books.views import search_form, search, contact, thanks

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
    (r'^search-form/$', search_form),
    (r'^search/$', search),
    (r'^contact/$', contact),
    (r'^contact/thanks/$', thanks)
)

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fdp.views.home', name='home'),
    url(r'^$', 'pontos.views.home', name='home'),
    url(r'^registro/novo$', 'pontos.views.novo', name='novo'),
    url(r'^registro/edit/(?P<pk>[0-9]+)$', 'pontos.views.edit', name='edit'),
    url(r'^registro/remove/(?P<pk>[0-9]+)$', 'pontos.views.remove', name='remove'),
    url(r'^accounts/registration/$', 'pontos.views.registration', name='registration'),
    url(r'^accounts/login/$', 'pontos.views.user_login', name='login'),
    url(r'^accounts/logout/$', 'pontos.views.user_logout', name='logout'),
    url(r'^mytimesheet/$', 'pontos.views.timesheet', name='timesheet'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fdp.views.home', name='home'),
    url(r'^$', 'pontos.views.home', name='home'),
    url(r'^novo-ponto$', 'pontos.views.novoponto', name='novoponto'),
    url(r'^novo$', 'pontos.views.novo', name='novo'),
    url(r'^registration/$', 'pontos.views.registration', name='registration'),
    url(r'^login/$', 'pontos.views.user_login', name='login'),
    url(r'^mytimesheet/$', 'pontos.views.timesheet', name='timesheet'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

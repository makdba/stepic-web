from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

      url(r'^$', 'qa.views.test', name='test'),
      url(r'^login/', 'qa.views.test', name='test'),
      url(r'^signup/', 'qa.views.test', name='test'),
      url(r'^question/(?P<q_id>\d+)/$', 'qa.views.question_info', name='question_info'),
      url(r'^ask/', 'qa.views.test', name='test'),
      url(r'^popular/', 'qa.views.test', name='test'),
      url(r'^new/', 'qa.views.test', name='test'),
    # url(r'^admin/', include(admin.site.urls)),
)

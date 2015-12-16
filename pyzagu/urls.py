from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'main.views.my_custom_404_view'


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^article/(?P<item>.*)/$', 'main.views.get_article', name='get_article'),
    url(r'^articles/$', 'main.views.articles'),
    url(r'^articles/(?P<page>\d+)/$', 'main.views.articles'),
    url(r'^news/$', 'main.views.news', name='all_news'),
    url(r'^news/(?P<page>\d+)/$', 'main.views.news', name='news'),
    url(r'^news-article/(?P<item>.*)/$', 'main.views.news_article', name='news_article'),
    url(r'^contacts/$', 'main.views.contacts', name='contacts'),
    url(r'^cabinet/$', 'main.views.cabinet', name='cabinet'),
    url(r'^calculation-programm/', 'main.views.calc_soft', name='calculation_programm'),
    url(r'^raschetnaya-programma/', 'main.views.calc_soft'),
    url(r'^feedback/$', 'main.views.feedback', name='feedback'),
    url(r'^robots.txt', 'main.views.robots'),
    url(r'^sitemap.xml', 'main.views.sitemap'),
    url(r'^colors-config/', 'main.views.colors_config'),
    url(r'^feedback/$', 'main.views.feedback', name='feedback'),
    url(r'^send-feedback/$', 'main.views.send_feedback', name='send_feedback'),
    url(r'^production/$', 'main.views.item_production', name='first_production'),
    url(r'^production/(?P<item>.*)/$', 'main.views.item_production', name='production'),#not implemented
    url(r'^catalog/(?P<url>.*)/$', 'main.views.catalog'),
    url(r'^catalog-item/(?P<url>.*)/$', 'main.views.catalog_item', name='catalog_item'),

    #url(r'^item_production/(\d+)/$', 'main.views.item_production'), # TODO need redirectview
    url(r'^projects/', 'main.views.projects', name='projects'),#not implemented
    url(r'^project/(?P<item>.*)/$', 'main.views.get_project', name='get_project'),#not implemented
    url(r'^for-partners/$', 'main.views.for_partners'),
    url(r'^for-partners/(?P<item>\d+)/$', 'main.views.for_partners'),
    url(r'^googlee288c274f02aaeea.html$','main.views.googlever2'),
    url(r'^googlecf83282b8297d084.html$','main.views.googlever'),

    # url(r'^pyzagu/', include('pyzagu.foo.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
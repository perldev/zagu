from django.conf.urls import *

from django.conf.urls.static import static
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'main.views.my_custom_404_view'


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home'),
    url(r'^index.html$', 'main.views.home'),
    url(r'^article/(\d+)$', 'main.views.article'),
    url(r'^articles/(\d+)$', 'main.views.articles'),
    url(r'^news/(\d+)$', 'main.views.news'),
    url(r'^news_article/(\d+)$', 'main.views.news_article'),
    url(r'^contacts$', 'main.views.contacts'),
    url(r'^cabinet$', 'main.views.cabinet'),
    url(r'^calculation_programm', 'main.views.calc_soft'),
    url(r'^raschetnaya-programma', 'main.views.calc_soft'), 
    url(r'^feedback$', 'main.views.feedback'),
    url(r'^robots.txt', 'main.views.robots'),
    url(r'^sitemap.xml', 'main.views.sitemap'),
    url(r'^colors_config', 'main.views.colors_config'),
    url(r'^feedback$', 'main.views.feedback'),
    url(r'^send_feedback$', 'main.views.send_feedback'),
    url(r'^production$', 'main.views.production'),#not implemented
    url(r'^catalog/([\w]+)$', 'main.views.catalog'),
    url(r'^catalog_item/([\w]+)$', 'main.views.catalog_item'),
    



    url(r'^item_production/(\d+)$', 'main.views.item_production'),#not implemented
    url(r'^projects', 'main.views.projects'),#not implemented
    url(r'^project/(\d+)', 'main.views.project'),#not implemented
    url(r'^for_partners/(\d+)$', 'main.views.for_partners'),    
    url(r'^article_partners/(\d+)$', 'main.views.article_partners'),   
    url(r'^robots.txt$', 'main.views.robots'),   
    url(r'^googlee288c274f02aaeea.html$','main.views.googlever2'),
    url(r'^googlecf83282b8297d084.html$','main.views.googlever'),
    

    # url(r'^pyzagu/', include('pyzagu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^\w+', "main.views.my_custom_404_view" )
)  

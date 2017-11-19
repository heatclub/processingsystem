from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #urls called by CMS app
    url(r'^insertdata/$', views.insertdata, name='insertdata'),
    #views.videos (views.<class name>)is a class
    url(r'^receivedata/$', views.receivedata, name='receivedata'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
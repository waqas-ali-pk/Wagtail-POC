"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, re_path, include

from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('polls/', include('polls.urls')),
    path('', include('main.urls')),

    re_path(r'', include(wagtail_urls)),

]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns() # tell gunicorn where static files are in dev mode
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
    urlpatterns += [
        path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'myapp/images/favicon.ico'))
    ]

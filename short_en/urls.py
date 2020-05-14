"""short_en URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path

from shortener.views import HomeView, URLRedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',HomeView.as_view()),
    # re_path(r'^(?P<shortcode>[\w-]+){6,15}/$',short_en_redirect_view),
    re_path(r'^(?P<shortcode>[\w-]+)/$',URLRedirectView.as_view(), name='scode'),
]


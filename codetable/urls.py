"""codetable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from code_editor.views import IndexView, CodeView, CodeEditor

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='home'),
	url(r'^code/(?P<code_id>.*)/$', CodeEditor.as_view(), name='code_editor'),
	url(r'^code$', CodeView.as_view(), name='code'),
    url(r'^admin/', include(admin.site.urls)),
]

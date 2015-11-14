"""project URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ratings_vote/$', 'ratings.views.vote', name='ratings_vote'),
    url(r'^/$','main.views.home'),
    url(r'^home/$','main.views.home'),
    url(r'^category/(?P<pk>\d+)/$', 'main.views.category_detail'),
    url(r'^recommendation/(?P<pk>\d+)/$', 'main.views.recommendation_detail'),
    url(r'^categories/$', 'main.views.category_list'),
    url(r'^cat_recommendations/(?P<pk>\d+)/$', 'main.views.cat_recommendations'),
    url(r'^location/(?P<pk>\d+)/$', 'main.views.location'),
    # url(r'^search/(?P<search>\w+)/$', 'main.views.search'),
    url(r'^submit/$', 'main.views.submit_email'),
    url(r'^user_signup/$','main.views.user_signup_view'),
    url(r'^business_signup/$','main.views.business_signup_view'),
    url(r'^business_submission/$','main.views.business_submission_view'),
    url(r'^user_login/$','main.views.user_login'),
    url(r'^business_login/$','main.views.business_login'),
    url(r'^user_profile/(?P<pk>\d+)$','main.views.user_profile_view'),
    url(r'^business_profile/(?P<pk>\d+)$','main.views.business_profile_view'),
    url(r'^voting/(?P<pk>\d+)$','main.views.voting'),
    url(r'^rate_me/$', 'main.views.rate_me'),
    url(r'^terms_of_use_and_privacy_policy/$','main.views.terms_of_use'),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# -*- coding: utf-8 -*-
'''
Root url routering file.

You should put the url config in their respective app putting only a
refernce to them here.
'''
from __future__ import unicode_literals

# Third Party Stuff
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^(?P<conference_slug>[\w-]+)/proposals/', include('proposals.proposal_urls')),
    url(r'^(?P<conference_slug>[\w-]+)/proposal-comments/', include('proposals.comment_urls')),
    url(r'^(?P<conference_slug>[\w-]+)/proposal-votes/', include('proposals.vote_urls')),

    url(r'^accounts/', include('allauth.urls')),
    url('^markdown/', include('django_markdown.urls')),

    # Static Pages
    url(r'^speakers/$', TemplateView.as_view(template_name='static-content/speakers.html',), name='speakers-static'),
    url(r'^schedule/$', TemplateView.as_view(template_name='static-content/schedule.html',), name='schedule-static'),
    url(r'^venue/$', TemplateView.as_view(template_name='static-content/venue.html',), name='venue-static'),
    url(r'^sponsors/$', TemplateView.as_view(template_name='static-content/sponsors.html',), name='sponsors-static'),
    url(r'^blog/$', TemplateView.as_view(template_name='static-content/blog-archive.html',), name='blog-archive'),
    url(r'^coc/$', TemplateView.as_view(template_name='static-content/coc.html',), name='coc-static'),
    url(r'^faq/$', TemplateView.as_view(template_name='static-content/faq.html',), name='faq_static'),
    url(r'^$', TemplateView.as_view(template_name='static-content/index.html',), name='home'),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^400/$', 'django.views.defaults.bad_request'),  # noqa
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    )

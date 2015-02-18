##
# YDNS Core
#
# Copyright (c) 2015 Christian Jurk <commx@commx.ws>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
##

from django.conf.urls import patterns, include, url
from .views import CreateView, DeleteView, DetailView, HomeView, JournalView, SettingsView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^new$', CreateView.as_view(), name='create'),
    url(r'^(?P<name>[\w\.-]+)/delete$', DeleteView.as_view(), name='delete'),
    url(r'^(?P<name>[\w\.-]+)/hosts/', include('domains.hosts.urls', namespace='hosts')),
    url(r'^(?P<name>[\w\.-]+)/journal$', JournalView.as_view(), name='journal'),
    url(r'^(?P<name>[\w\.-]+)/mq/', include('domains.mq.urls', namespace='mq')),
    url(r'^(?P<name>[\w\.-]+)/settings$', SettingsView.as_view(), name='settings'),
    url(r'^(?P<name>[\w\.-]+)/$', DetailView.as_view(), name='detail'),
)
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path
from api import views

urlpatterns = [
	re_path(r"^messages/?$", views.MessageList.as_view(), name='message-list'),
	re_path(r"^messages/(?P<pk>\d+)/?$", views.MessageDetail.as_view(), name='message-by-id'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

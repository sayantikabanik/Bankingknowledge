from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DetailView, ListView

urlpatterns = {
    url(r'^ifscCode/(?P<ifsc>[A-Za-z]{4}\w{7})$', DetailView.as_view()),
    url(r'^branchesCity/(?P<city>.*)/(?P<bank>.*)$', ListView.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)
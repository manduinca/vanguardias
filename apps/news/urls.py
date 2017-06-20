from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^news$', TemplateView.as_view(template_name='news.html')),
]

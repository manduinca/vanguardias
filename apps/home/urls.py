from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^', TemplateView.as_view(template_name='home.html')),
    url(r'^home', TemplateView.as_view(template_name='home.html')),
]

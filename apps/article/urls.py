from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^article$', TemplateView.as_view(template_name='article.html')),
]

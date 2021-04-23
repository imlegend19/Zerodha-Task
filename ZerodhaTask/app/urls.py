from django.urls import path
from django.views.generic import TemplateView

from ZerodhaTask.app.views import *

urlpatterns = [
    path('api/search/<str:query>', search),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

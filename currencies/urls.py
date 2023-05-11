from django.urls import path 
from . import views



urlpatterns = [
    path('', views.latest_news, name = 'latest_news'),
    path('top_performers', views.top_performers, name = 'top_performers'),
    path('render_stats', views.render_stats, name = 'render_stats'),
    path('main', views.main, name = 'main'),
    path('login', views.login_view, name = 'login')
]
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('home/', views.homepage),
    # path('about/', views.about),
    path('', views.posts_list),
]
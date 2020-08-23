from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('blog.urls')),
    path('api/', include('analytics.urls')),

    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]

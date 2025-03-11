from  django.contrib import admin
from django.urls import include, path

api_urls = [
    path('', include('users.urls')),
    path('pets', include('pets.urls')),
]




urlpatterns = [
    path('api/v1/pets/', include('pets.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
]
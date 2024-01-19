from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Fortune_app.urls')),  # 'Fortune_app' 앱의 urls.py 포함
]

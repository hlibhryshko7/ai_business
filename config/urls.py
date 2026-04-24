from django.contrib import admin
from django.urls import path, include
# Импортируем функцию для мультиязычных маршрутов
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('ai-secret-panel/', admin.site.urls),  
    path('', include('main_app.urls')),         
)
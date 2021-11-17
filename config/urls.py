from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('RestApi/', include('rest_framework.urls')),
    path('decks/', include('apps.decks.urls')),
    path('cards/', include('apps.cards.urls')),
]

from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owner', OwnerViewSet)

urlpatterns = [
    # Для rest_framework.authtoken
    # path('api-token-auth/', views.obtain_auth_token),

    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),

    path('', include(router.urls)),
]

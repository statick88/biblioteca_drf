from django.urls import path, include
from rest_framework.routers import DefaultRouter
from libros.views import LibroViewSet, AutorViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API de Biblioteca",
        default_version='v1',
        description="API para administrar una biblioteca de libros y autores.",
    ),
    public=True,
)

router = DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'autores', AutorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
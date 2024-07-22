from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CountryListCreateAPIView, CountryDetailAPIView, CarListCreateView, CarDetailView, PartsViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'parts', PartsViewSet)

urlpatterns = [
    path('api/countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('api/countries/<int:pk>/', CountryDetailAPIView.as_view(), name='country-detail'),
    path('api/cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('api/cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]
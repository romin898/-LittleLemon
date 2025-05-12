#define URL route for index() view
from django.urls import path
from .views import index,MenuItemView,SingleMenuItemView,BookingViewSet
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view(),name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]
urlpatterns += router.urls
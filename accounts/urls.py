from django.urls import path
from rest_framework.routers import DefaultRouter
from accounts import views

router = DefaultRouter()
router.register('Customers',views.CustomerViewSet)
router.register('Update-Customers',views.CustomerUpdateViewSet)
router.register('Get-Customers/(?P<tracking_code>\d+)',views.GetCustomerViewSet)
router.register('Get-All-Customers',views.AdminGetCustomerViewSet)
urlpatterns = [
]
urlpatterns += router.urls

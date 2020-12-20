from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,DjangoModelPermissions
from rest_framework.response import Response
from rest_framework import status
from .models import Customers
from .serializers import CustomersSerializer,CustomersUpdateSerializer,GetCustomersSerializer
from rest_framework import viewsets
from django.core.cache import cache

#register Customers
class CustomerViewSet (viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    http_method_names = ['post']
    permission_classes = (AllowAny, )

    def create (self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        if (request.data['national_code']).isnumeric() and len(request.data['national_code']) == 10 :
            instance = obj.data
            return Response ({'tracking_code' : instance['tracking_code']})
        else :
            return Response ({'tracking_code' : ''},status = status.HTTP_400_BAD_REQUEST)
# Update Customers
class CustomerUpdateViewSet (viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersUpdateSerializer
    http_method_names = ['get','put']

    def create (self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        return obj

# get Customers data by tracking code
class GetCustomerViewSet (viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = GetCustomersSerializer
    http_method_names = ['get']
    permission_classes = (AllowAny, )
    def get_queryset(self):
        user = self.request.user
        customers_obj = cache.get(self.kwargs['tracking_code'])
        check = bool (customers_obj)
        if check : # if customer exist in cache
            customers = {customers_obj}
        else :  # if customer not exist in cache
            customers = Customers.objects.filter(tracking_code=self.kwargs['tracking_code'])
        return customers

# get all Customers by admin user
class AdminGetCustomerViewSet (viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    http_method_names = ['get']
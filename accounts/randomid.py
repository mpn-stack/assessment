from .models import Customers
import datetime 



def get_random_number():
    get_date = datetime.datetime.now()
    get_date_int = int(get_date.strftime("%Y%m%d%H%M%S"))
    try :
        customer_tracking_code = Customers.objects.all().count()
        customer_tracking_code =str(get_date_int)+str(customer_tracking_code)
    except :
        customer_tracking_code = str(get_date_int)+'1'
    return customer_tracking_code
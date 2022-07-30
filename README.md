#1 - register Customer
curl --location  --request POST '127.0.0.1:8000/Customers/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "alireza",
    "last_name": "ghomei",
    "national_code": "0559867158"
}'

#2 - get customer data with trakingnumber
curl --location --request GET '127.0.0.1:8000/Get-Customers/2020122017012935'


#3 - get token for admin user
curl --location --request POST '127.0.0.1:8000/api-token-auth' \
--form 'username="admin"' \
--form 'password="123456"'

#4 - update customer data
curl --location --request PUT '127.0.0.1:8000/Update-Customers/30/' \
--header 'Authorization: Token 713a846e18a5d0755970b1b2e08f2980b1c8cfff' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "aliakbar",
    "last_name": "hakimi",
    "national_code": "0559867122",
    "status": 2
}

#5 - get all customers data by admin user
curl --location --request GET '127.0.0.1:8000/Get-All-Customers' \
--header 'Authorization: Token 713a846e18a5d0755970b1b2e08f2980b1c8cfff' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name" : "shahin ",
    "last_name" : "nabavi",
    "national_code" : "0559867111"
}'

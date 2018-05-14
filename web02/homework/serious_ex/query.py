from models.customer import Customer
import mlab
mlab.connect()

all_customer = Customer.objects(gender=1)

# first_service = all_service[0]
for index, Customer in enumerate(all_customer):
    print(Customer['name'])
    if index == 9:
        break
# print(first_service['name'])

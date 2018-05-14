from models.customer import Customer
from faker import Faker
import mlab
from random import randint, choice
fake = Faker()
mlab.connect()
for i in range(50):
    print("Saving customer", i + 1, "..." )
    customer = Customer(name=fake.name(), yob=randint(1990, 2001), gender=randint(0, 1), height=randint(150, 190),
                      phone=fake.phone_number(), address=fake.address(), status=choice([True, False]))
    customer.save()


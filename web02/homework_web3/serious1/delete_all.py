

from models.service import Service
import mlab

mlab.connect()

item = Service.objects()

for i in item:
    if i is not None:
        i.delete() 
        print('Deleting item ....')
    else:
        print("service not found")

from models.service import Service
import mlab 
mlab.connect()

all_service = Service.objects(gender=1)

# first_service = all_service[0]
for index, service in enumerate(all_service):
    print(service['name'])
    if index == 9:
        break
# print(first_service['name'])





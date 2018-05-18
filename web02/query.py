from models.service import Service
import mlab 
mlab.connect()

id_to_find = "5af59ce73a6295114440d678"

misthy = Service.objects.with_id(id_to_find)

if misthy is not None:
    # hera.delete()
    # print("Deleted")
    print(misthy.address)
    misthy.update(set__address="Bac Co", set__height=175)
    misthy.reload()
    print(misthy.address)
else:
    print("Service not found")

# print(hera.to_mongo())
# all_service = Service.objects(gender=1)

# # first_service = all_service[0]
# for index, service in enumerate(all_service):
#     print(service['name'])
#     if index == 9:
#         break
# print(first_service['name'])





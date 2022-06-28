from models import *

# dist = Income(12,1)
# dist.save()

# set = Student.get_by_id(2)
# set.Marks = 55
# set.save()

# delet
# set = Student.get_by_id(1)
# hell = Student.delete(set)


for dist in Countries.objects():
   print(dist)



# stud = Class.get_by_id(1)
# stud.name = "10 B"
# stud.save()
import pdb 
from models.task import Task
import repositories.task_repository as task_repository  

from models.user import User
import repositories.user_repository as user_repository

task_repository.delete_all()
user_repository.delete_all()

user_1 = User("Victor", "McDade")
user_2 = User("Jack", "Jarvis")

user_repository.save(user_1)
user_repository.save(user_2)

new_task = Task("Go for a run", user_1, 20)
task_repository.save(new_task)

task_1 = Task("Walk Dog", user_1, 60)
task_repository.save(task_1)

task_2 = Task("Feed Cat", user_2, 5)
task_repository.save(task_2)


# # task_repository.delete_one(new_task.id)

# task_2.mark_complete()
# task_repository.update(task_2)

result = task_repository.select_all()

for task in result:
    print(task.user.__dict__)

# found_task = task_repository.select(task_2.id)
# print(found_task.__dict__)



# pdb.set_trace()
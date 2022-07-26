import pdb 
from models.task import Task
import repositories.task_repository as task_repository  

task_repository.delete_all()

new_task = Task("Go for a run", "Jack Jarvis", 20)
task_repository.save(new_task)

task_1 = Task("Walk Dog", "Ada Lovelace", 60)
task_repository.save(task_1)

task_2 = Task("Feed Cat", "Victor McDade", 5)
task_repository.save(task_2)

# task_repository.delete_one(new_task.id)

task_2.mark_complete()
task_repository.update(task_2)

result = task_repository.select_all()

for task in result:
    print(task.__dict__)

found_task = task_repository.select(task_2.id)
print(found_task.__dict__)



pdb.set_trace()
from . import taskAdd

class TaskShow(taskAdd.TaskAdd):
    def __init__(self, taskList, id, description):
        taskAdd.TaskAdd.__init__(taskList,id,description)


    def show(self):
        for task in self.tasks:
            print(task.id + " " + task.description)
            if task.isDone():
                print ("Task Done")
            else:
                print("Task NOT Done")
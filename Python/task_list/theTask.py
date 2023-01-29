from . import taskId
from . import taskDescription
from . import taskDone

# Classe correspondant à une tache avec tous ses attributs
# Elle hérite de taskId taskDescription et taskDone
class TheTask(taskId.TaskId, taskDescription.TaskDescription, taskDone.TaskDone):
    def __init__(self, id, description, done):
        taskId.TaskId.__init__(self, id)
        taskDescription.TaskDescription.__init__(self, description)
        taskDone.TaskDone.__init__(self, done)

#   Permet de connaître la valeur de done
    def Done(self):
        if self.done:
            return True
        return False
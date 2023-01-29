from . import taskId
from . import taskDescription
from . import taskDone


class TheTask(taskId.TaskId, taskDescription.TaskDescription, taskDone.TaskDone):
    def __init__(self, id, description, done):
        taskId.TaskId.__init__(self, id)
        taskDescription.TaskDescription.__init__(self, description)
        taskDone.TaskDone.__init__(self, done)

    def Done(self):
        if self.done:
            return True
        return False
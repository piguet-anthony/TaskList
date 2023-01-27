from . import taskId
from . import taskDescription


class TaskAdd(taskId.TaskId, taskDescription.TaskDescription):
    def __init__(self, id, description, done):
        taskId.TaskId.__init__(self, id)
        taskDescription.TaskDescription.__init__(self, description)
        self.done = done
        self.last_id: int = 0
        self.tasks = dict()

    def add_new_task(self):
        self.tasks[self.last_id] = self.description

    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def isDone(self):
        if self.done:
            return True
        return False
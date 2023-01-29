from . import theTask

class TaskAdd(theTask.TheTask):
    def __init__(self, id, description, done):
        super().__init__(id, description, done)
        self.last_id: int = 0
        self.tasks = list()

    def add_new_task(self):
        self.tasks = theTask.TheTask(self.last_id, self.description, self.done)

    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id
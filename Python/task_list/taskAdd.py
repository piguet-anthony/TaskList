import taskId
import taskDescription

class TaskAdd(taskId.TaskId, taskDescription.TaskDescription):
    def __init__(self, id: int, description: str) -> None:
        taskId.TaskId.__init__(self,id)
        taskDescription.TaskDescription.__init__(self,description)
        self.last_id: int = 0
        self.tasks = list()

    def ajout_de_tache(self, description: str) -> None:
        self.__init__(self.next_id(), description)

    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

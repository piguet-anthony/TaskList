import taskId
import taskDescription

class TaskShow(taskId.TaskId, taskDescription.TaskDescription):
    def __init__(self, id: int, description: str) -> None:
        taskId.TaskId.__init__(self,id)
        taskDescription.TaskDescription.__init__(self,description)



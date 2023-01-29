from . import taskAdd

class TaskShow(taskAdd.TaskAdd):
    def __init__(self, id, description, done):
        super().__init__(id, description, done)

    def show(self):
        for task in self.list_of_task:
            affichageFinal = str(task.id) + " " + str(task.description) + "etat : "
            etat = "NOT Check"
            if task.done:
                etat = "Check"
            print(affichageFinal + etat)
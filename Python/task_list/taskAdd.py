from . import theTask

# Classe permettant l'ajout d'une tache dans la liste
# Elle hérite de theTask
class TaskAdd(theTask.TheTask):
    def __init__(self, id, description, done):
        super().__init__(id, description, done)
        self.last_id: int = 0       # valeur permettant d'incrémanter l'unique ID des taches suivantes
        self.list_of_task = list()  # les taches seront dans cette liste

#   Ajout de la tache dans la liste
    def add_new_task(self):
        self.list_of_task = theTask.TheTask(self.last_id, self.description, self.done)
        self.next_id()

#   Fonction qui incrémante ID
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id
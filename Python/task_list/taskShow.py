from . import taskAdd

# Classe permettant d'afficher la liste avec les taches à l'interrieur
# Elle hérite de taskAdd
class TaskShow(taskAdd.TaskAdd):
    def __init__(self, id, description, done):
        super().__init__(id, description, done)

#   Fonction qui parcours list_of_task et qui affiche simplement les taches avec l'id, la description et si elle est fini ou pas
    def show(self):
        for task in self.list_of_task:
            affichageFinal = str(task.id) + " " + str(task.description) + "etat : "
            etat = "NOT Check"
            if task.done:
                etat = "Check"
            print(affichageFinal + etat)
#/!\/!\     Je me suis trouvé nez-à-nez avec une erreur que je n'ai pas réussi à corriger :
#               AttributeError: type object 'TaskAdd' has no attribute 'list_of_task'
#           Je ne comprend pas bien pourquoi TaskAdd n'a pas d'attribut list_of_task alors que je fait un héritage sur taskAdd
#           et que dans la class TaskAdd il y a bien ma variable list_of_task à la ligne 9 de taskAdd.py

# Si vous avez une peu de temps à m'accorder, pourriez-vous m'expliquer quel est ce problème et comment le corriger. Merci par avance
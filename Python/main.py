import task_list.taskId as taskId
import task_list.taskDescription as taskDescription
import task_list.taskAdd as taskAdd
import task_list.taskShow as taskShow

id_of_task = taskId.TaskId(1)
description_of_task = taskDescription.TaskDescription("une description")
list_of_task = taskAdd.TaskAdd(id_of_task.id,description_of_task.description)
taskAdd.TaskAdd.add_new_task(list_of_task)

show_the_list = taskShow.TaskShow(list_of_task, id_of_task.id, description_of_task.description)
show_the_list.show()
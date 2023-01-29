import task_list.taskId as taskId
import task_list.taskDescription as taskDescription
import task_list.taskAdd as taskAdd
import task_list.taskShow as taskShow

id_of_task = taskId.TaskId(0)
description_of_task = taskDescription.TaskDescription("une description")
une_task = taskAdd.TaskAdd(id_of_task.id,description_of_task.description, False)

taskAdd.TaskAdd.add_new_task(une_task)

taskShow.TaskShow.show(taskAdd.TaskAdd)
from task_end.task_struct import Task

def create_task(task: Task) -> dict:
    return Task.model_dump(task)

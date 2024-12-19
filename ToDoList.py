from Task import Task


class ToDoList:
    def __init__(self):
        self.tasks = []

    def findTaskIndex(self, title):
        for i in range(len(self.tasks)):
            if self.tasks[i].title == title:
                return i
        return None

    def add_task(self, title, description, priority):
        i = self.findTaskIndex(title)
        if i is not None:
            print("task already exists")
            return
        self.tasks.append(Task(title, description, priority))

    def remove_task(self, title):
        i = self.findTaskIndex(title)
        if i is None:
            print("task not found")
            return
        self.tasks.pop(i)

    def view_sorted_tasks(self):
        for t in sorted(self.tasks, key= lambda x: x.title):
            print("title:", t.title, "desc:", t.description, "prio:", t.priority, "is_completed:", t.is_completed)

    def mark_as_completed(self, title):
        i = self.findTaskIndex(title)
        if i is None:
            print("task not found")
            return

        self.tasks[i].is_completed = True

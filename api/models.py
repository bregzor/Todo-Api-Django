from django.db import models

class TaskList(models.Model):
    name = models.CharField(max_length=250)
    # dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskItem(models.Model):
    task_id = models.AutoField(primary_key=True)
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=600, blank=True)
    isCompleted = models.BooleanField(default=False)


    def __str__(self):
        return self.title
 
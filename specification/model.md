```Python
class Users(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(
        default=1,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    bio = models.CharField(max_length=420, default="Nothing for him/her", blank=True)
    avatar = models.ImageField(upload_to="xxx", default="xxx", blank=True)
    notification = models.BooleanField(default = "True") # on/off the notification
    Group = models.ManyToManyField(Group)

class Group(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)

class Project(models.Model):
    project_name = models.CharField(max_length=420, default="", blank=True)
    date_of_creation = models.DateField(auto_now_add = true)
    deadline = models.DateField()
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)
    finished = models.BooleanField(default = "False") # whether the project has finished on time
 
class Task(models.Model):
    task_name = models.CharField(max_length=420, default="", blank=True)
    date_of_creation = models.DateField(auto_now_add = True)
    deadline = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) # the user responsible for this task
    description = models.CharField(max_length=420, default="", blank=True)
    finished = models.BooleanField(default = "False") # whether the task has finished on time
```


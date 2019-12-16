from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.title

class NotesTask(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Assignment(models.Model):
    notes = models.ForeignKey("notulen.Notes", on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    task = models.ForeignKey("notulen.NotesTask", on_delete=models.CASCADE)

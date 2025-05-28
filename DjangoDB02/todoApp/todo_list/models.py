from django.db import models

class todo(models.Model):
    title = models.CharField(max_length=200)
    iscompleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.iscompleted) + ' | ' + str(self.created_at.strftime('%d/%m/%Y %H:%M:%S'))
    


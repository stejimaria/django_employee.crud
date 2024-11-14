from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField()
    ename=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.TextField()
    email=models.EmailField()
    image=models.ImageField(upload_to="images",blank=True,null=True)

    def __str__(self):
        return self.ename

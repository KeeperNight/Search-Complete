from django.db import models
from book.models import Book
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default ='default.png',upload_to = 'Profile_pics')
    books = models.ManyToManyField(Book, through='Read')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Read(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    STATUS = (('C','Completed'),('R','Reading...'),('CC','Yet to complete'),('NS','Not Started'))
    read_status = models.CharField(choices = STATUS, max_length=4)
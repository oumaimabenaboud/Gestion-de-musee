from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
user = get_user_model()
class abonne(models.Model):
    username = models.ForeignKey(user, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    type = models.IntegerField()


    def __str__(self):
        return self.user.username
class Registrationform (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
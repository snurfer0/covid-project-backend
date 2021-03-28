from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# Create your models here.


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(
        'auth.User', related_name='tests', on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='images', blank=False, null=False, default=None)
    isPositive = models.BooleanField(null=False, default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

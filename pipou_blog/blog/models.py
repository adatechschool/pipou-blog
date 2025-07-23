from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=255, verbose_name='Titre')
  content = models.TextField(verbose_name='Contenu')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  class Meta:
    verbose_name = 'Publication'
    verbose_name_plural = 'Publications'
    ordering = ['-created_at']

  def __str__(self):
    return self.title

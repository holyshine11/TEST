from django.db import models

class MBTIFortune(models.Model):
    mbti = models.CharField(max_length=4, unique=True)
    fortune = models.TextField()

    def __str__(self):
        return self.mbti

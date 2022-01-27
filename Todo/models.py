from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField( max_length=50)

    

    # class Meta:
    #     verbose_nam")
    #     verbose_name_pluras")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return re_detail", kwargs={"pk": self.pk})

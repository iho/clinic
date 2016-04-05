from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Reception(models.Model):
    date = models.DateField(blank=False)
    hour = models.PositiveSmallIntegerField(
            choices=[(i,i) for i in range(9, 18) ] 
            )
    doctor = models.ForeignKey(Doctor)
    full_name = models.TextField()

    class Meta:
        unique_together = ("date", "hour", "doctor")

    def __str__(self):
        return str(self.date)+ ' : ' + self.doctor.name 



from django.db import models


class Applicant(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    TIME_CHOICES = (
        ('8:00AM', '8:00AM'),
        ('9:00AM', '9:00AM'),
        ('10:00AM', '10:00AM'),
        ('11:00AM', '11:00AM'),
        ('12:00PM', '12:00PM'),
        ('1:00PM', '1:00PM'),
        ('2:00PM', '2:00PM'),
        ('3:00PM', '3:00PM'),
        ('4:00PM', '4:00PM'),
        ('5:00PM', '5:00PM'),
    )


    # STATUS_CHOICES = (
    #     ('PENDING', 'Pending'),
    #     ('APPROVED', 'Approved'),
    #     ('REJECTED', 'Rejected')
    # )

    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    income = models.CharField(max_length=200)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    appdate = models.CharField(max_length=20)
    apptime = models.CharField(max_length=20, choices=TIME_CHOICES)
    status = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


# Create your models here.

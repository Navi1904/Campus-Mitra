from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Hr(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)


class JobPost(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    compnayName = models.CharField(max_length=100)
    companyLogoUrl = models.URLField(max_length=500, blank=True, null=True)
    companyDescription = models.TextField(blank=True, null=True)
    salaryLow = models.IntegerField(default=0)
    salaryHigh = models.IntegerField(default=0)
    applyCount = models.IntegerField(default=0)
    lastDateToApply = models.DateField()

    def __str__(self):
        return str(self.title)


STATUS_CHOICE = (
    ('pending','pending'),
    ('selected','selected')
)

class CandidateApplications(models.Model):
    
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    job = models.OneToOneField(to=JobPost,on_delete=models.CASCADE)
    
    passingYear = models.IntegerField()
    yearOfExp = models.IntegerField(default=0)
    resume = models.FileField(upload_to='resume')
    cgpa=models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICE,max_length=20,default='pending')

    def __str__(self):
        return str(self.user.username)+" "+str(self.job.title)



class SelectCandidateJob(models.Model):
    job = models.ForeignKey(to=JobPost,on_delete=models.CASCADE)
    candidate = models.OneToOneField(to=CandidateApplications,on_delete=models.CASCADE)


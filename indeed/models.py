from django.db import models


# Create your models here.
class IndeedReview(models.Model):
    companyName = models.CharField(max_length=30, null=True)
    companyDesc = models.TextField(null=True)
    overallRating = models.CharField(max_length=10, null=True)
    totalReviews = models.CharField(max_length=10, null=True)
    workLifeBalance = models.CharField(max_length=10, null=True)
    payAndBenefits = models.CharField(max_length=10, null=True)
    jobSecurity = models.CharField(max_length=10, null=True)
    management = models.CharField(max_length=10, null=True)
    culture = models.CharField(max_length=10, null=True)
    reviewHeadings = models.TextField(null=True)
    reviewDescriptions = models.TextField(null=True)
    reviewPros = models.TextField(null=True)
    reviewCons = models.TextField(null=True)
    reviewDate = models.TextField(null=True)
    companyUrl = models.TextField(null=True)

    def __str__(self):
        return self.companyName

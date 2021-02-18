from django.db import models


# Create your models here.
class GlassdoorReview(models.Model):
    companyName = models.CharField(max_length=30, null=True)
    companyDesc = models.TextField(null=True)
    companyJobs = models.CharField(max_length=10, null=True)
    companyInterviews = models.CharField(max_length=10, null=True)
    companyBenefits = models.CharField(max_length=10, null=True)
    overallRating = models.CharField(max_length=10, null=True)
    totalReviews = models.CharField(max_length=10, null=True)
    recommendToFriend = models.CharField(max_length=10, null=True)
    approveOfCEO = models.CharField(max_length=10, null=True)
    overallPros = models.TextField(null=True)
    overallCons = models.TextField(null=True)
    reviewHeadings = models.TextField(null=True)
    reviewDescriptions = models.TextField(null=True)
    reviewPros = models.TextField(null=True)
    reviewCons = models.TextField(null=True)
    reviewDate = models.TextField(null=True)

    def __str__(self):
        return self.companyName

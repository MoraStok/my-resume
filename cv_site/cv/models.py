from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=100, verbose_name="Job Name")
    company_name = models.CharField(max_length=100, verbose_name="Company Name")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(null=True, blank=True, verbose_name="End Date")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

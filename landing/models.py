from django.db import models


class Job(models.Model):
    # job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=64)
    start_date = models.DateField(blank=True)  # TODO will this cause problems for camp etc?
    end_date = models.DateField(blank=True)
    supervisor = models.CharField(max_length=64, blank=True)
    description = models.TextField(blank=True)
    company_id = models.ForeignKey('Company', on_delete=models.SET_DEFAULT, default=1)
    display_on_site = models.BooleanField()

    def __str__(self):
        return self.job_title


class Company(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    address_line_one = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=32, blank=True)
    state = models.CharField(max_length=2, blank=True)
    years_affiliated = models.CharField(max_length=64, blank=True)  # for descriptive times <1 year, every summer, etc.

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

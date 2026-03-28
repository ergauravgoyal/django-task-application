from task_app.job_app.models import Job
from django.db import models


class Application(models.Model):
    STATUS_CHOICES = [
        ("applied", "Applied"),
        ("in_review", "In Review"),
        ("interviewing", "Interviewing"),
        ("on_hold", "On Hold"),
        ("hired", "Hired"),
        ("joined", "Joined"),
    ]

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications",
        db_column="job_id",
    )
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()
    applicant_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="applied"
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "applications"

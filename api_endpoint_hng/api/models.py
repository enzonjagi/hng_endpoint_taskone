from django.db import models

# Create your models here.

class Info(models.Model):
    """
    Model to store the required data:
    
    Attributes:
        - slack_name
        - track
        - github_username
        - github_repo
        - github_file
    """

    slack_name = models.CharField(max_length=255)
    track = models.CharField(max_length=255)
    github_username = models.CharField(max_length=255)
    github_repo = models.CharField(max_length=255)
    github_file = models.CharField(max_length=255)

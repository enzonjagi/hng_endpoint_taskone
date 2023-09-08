from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Info
from .serializers import InfoSerializer
import datetime
import pytz

class GetInfo(APIView):
    """A View for the JSON Information needed

    by Njagi Ndungo
    
    Methods:
        - get: Get the required request info, from the url and display in the view.

        The Information shared in the url reflects in the request below.
    
    """

    def get(self, request):
        """Get the required JSON info and display in the view."""

        slack_name = request.query_params.get('slack_name')
        track = request.query_params.get('track')
        github_username = request.query_params.get('github_username')
        github_repo = request.query_params.get('github_repo')
        github_file = request.query_params.get('github_file')


        if None in [slack_name, track, github_username, github_repo, github_file]:
            return Response({
                "error": "All parameters are required."
            },
            status=status.HTTP_400_BAD_REQUEST)
        
        # Get the current day of the week info
        today = datetime.datetime.now(pytz.UTC).strftime('%A')

        # Get current time in UTC with a plus or minus 2 hours
        time_now = datetime.datetime.now(
            pytz.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')
        
        # Adding the info to the DB
        Info.objects.create(
            slack_name=slack_name,
            track=track,
            github_username=github_username,
            github_repo=github_repo,
            github_file=github_file,
        )

        response_data = {
            "slack_name": slack_name,
            "current_day": today,
            "utc_time": time_now,
            "track": track,
            "github_file_url": f"https://github.com/{github_username}/{github_repo}/blob/main/{github_file}",
            "github_repo_url": f"https://github.com/{github_username}/{github_repo}",
            "status_code": status.HTTP_200_OK
        }

        return Response(response_data, status=status.HTTP_200_OK)


#!/usr/bin/python3
#
# script to create pull requests on a locally hosted Bitbucket Server.
#

import requests
import json
import urllib3
import sys

# --- Get Branch Information from Command Line Arguments ---
if len(sys.argv) != 4:
    print("Usage: python create_pull_request.py <repo> <source_branch> <destination_branch>")
    sys.exit(1)

# --- Configuration ---
bitbucket_server_url = "https://example.com"
project_key = "<proj key>"
username = "<username>"
password = "<passwd>"

repo_slug = sys.argv[1]
source_branch = sys.argv[2]
destination_branch = sys.argv[3]


# Suppress the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- Pull Request Data ---
pull_request_data = {
    "title": f"Merge of {source_branch} into {destination_branch}",
    "description": "Modifications in support of pull request",
    "fromRef": {
        "id": f"{source_branch}"
    },
    "toRef": {
        "id": f"{destination_branch}"
    },
    "reviewers": [
        {
            "user": {
                "name": "user0"
            }
        },
        {
            "user": {
                "name": "user1"
            }
        }
    ]
}

# --- API Endpoint ---
api_endpoint = f"{bitbucket_server_url}/rest/api/1.0/projects/{project_key}/repos/{repo_slug}/pull-requests"

# --- Make the Request (Insecurely) ---
response = requests.post(
    api_endpoint,
    auth=(username, password),
    headers={"Content-Type": "application/json"},
    data=json.dumps(pull_request_data),
    verify=False  # Disable SSL verification
)

# --- Handle the Response ---
if response.status_code == 201:
    print("Pull request created successfully!")
    print(response.text)  # Print the response from Bitbucket Server
else:
    print(f"Error creating pull request: {response.status_code}")
    print(response.text)  # Print the error message

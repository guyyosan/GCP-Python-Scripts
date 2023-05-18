# GCP-Python-Scripts

## Getting started
Install requirements
`python3 -m venv .venv`
`source .venv/bin/activate`
`pip install requirements`

### Cloud Run
#### delete_revisions.py
`python cloudrun/delete_revisions.py -p <Project ID> -l <Region> -s <Cloud Run Service Name> -k <Revisions to keep> `

Manage Google Cloud Run revisions.

options:
  -h, --help            show this help message and exit
  -p PROJECT_ID, --project-id PROJECT_ID
                        Google Cloud project ID.
  -l LOCATION, --location LOCATION
                        Google Cloud region.
  -s SERVICE, --service SERVICE
                        Cloud Run service name.
  -k KEEP, --keep KEEP  Number of revisions to keep. Must be at least 10.
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

options:<br/>
  -h, --help            show this help message and exit<br/>
  -p PROJECT_ID, --project-id PROJECT_ID<br/>
                        Google Cloud project ID.<br/>
  -l LOCATION, --location LOCATION<br/>
                        Google Cloud region.<br/>
  -s SERVICE, --service SERVICE<br/>
                        Cloud Run service name.<br/>
  -k KEEP, --keep KEEP  Number of revisions to keep. Must be at least 10.<br/>

# GCP-Python-Scripts

## Getting started
Install requirements<br/>
`python3 -m venv .venv`<br/>
`source .venv/bin/activate`<br/>
`pip install requirements`<br/>

### Cloud Run
#### delete_revisions.py
`python cloudrun/delete_revisions.py -p <Project ID> -l <Region> -s <Cloud Run Service Name> -k <Revisions to keep> `

Manage Google Cloud Run revisions.

options:<br/>
&nbsp;&nbsp;-h, --help&nbsp;&nbsp;&nbsp;&nbsp;show this help message and exit<br/>
&nbsp;&nbsp;-p PROJECT_ID, --project-id PROJECT_ID<br/>
&nbsp;&nbsp;-l LOCATION, --location LOCATION<br/>
&nbsp;&nbsp;-s SERVICE, --service SERVICE<br/>
&nbsp;&nbsp;-k KEEP, --keep KEEP  Number of revisions to keep. Must be at least 10.<br/>

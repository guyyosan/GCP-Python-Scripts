from google.cloud import run_v2
import argparse


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Manage Google Cloud Run revisions.')
    parser.add_argument("-p", "--project-id", type=str, required=True,
                        help="Google Cloud project ID.")
    parser.add_argument("-l", "--location", type=str, default='us-central1',
                        help="Google Cloud region.")
    parser.add_argument("-s", "--service", type=str, required=True,
                        help="Cloud Run service name.")
    parser.add_argument("-k", "--keep", type=int, default=30,
                        help="Number of revisions to keep. Must be at least 10.")
    return parser.parse_args()


def extract_conditions(rev):
    """Extract conditions from revision and return as a dictionary."""
    conditions = {}
    while len(rev.conditions):
        condition = rev.conditions.pop()
        conditions[condition.type_] = {"state": condition.state, "message": condition.message}
    return conditions


def main():
    args = parse_args()

    client = run_v2.RevisionsClient()

    # Initialize arguments
    project = args.project_id.strip()
    location = args.location.strip()
    service = args.service.strip()

    print(f"Project ID: {project}")
    list_request = run_v2.ListRevisionsRequest(
        parent=f"projects/{project}/locations/{location}/services/{service}"
    )

    # Fetch the revisions
    revisions = client.list_revisions(request=list_request)

    active_revision = None
    revisions_to_keep = []
    revisions_to_keep_count = max(args.keep, 10)  # Ensure we keep at least 10 revisions

    for revision in revisions:
        if len(revisions_to_keep) < revisions_to_keep_count:
            conditions = extract_conditions(revision)

            if not active_revision and not conditions["Active"]["message"] and \
                    conditions["Active"]["state"] == run_v2.Condition.State.CONDITION_SUCCEEDED:
                active_revision = revision.name
                revisions_to_keep.append(revision.name)

            if conditions["Ready"]["message"] == "Revision retired." and \
                    conditions["Ready"]["state"] == run_v2.Condition.State.CONDITION_SUCCEEDED:
                revisions_to_keep.append(revision.name)
        else:  # Delete the revision
            delete_request = run_v2.DeleteRevisionRequest(name=revision.name)
            operation = client.delete_revision(request=delete_request)
            print(f"Deleting {revision.name.split('/')[-1]}. Waiting for operation to complete...")
            operation.result()

    print(f"Revisions to keep: {[r.split('/')[-1] for r in revisions_to_keep]}")


if __name__ == "__main__":
    main()

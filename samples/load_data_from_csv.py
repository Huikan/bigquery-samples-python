from samples.utils import get_service, poll_job
import json
import uuid


# [START load_table]
def load_table(service, source_schema, source_csv,
               projectId, datasetId, tableId, num_retries=5):
    # Generate a unique job_id so retries
    # don't accidentally duplicate query
    job_data = {
            'jobReference': {
                    'projectId': projectId,
                    'job_id': str(uuid.uuid4())
                    },
            'configuration': {
                    'load': {
                            'sourceUris': [source_csv],
                            'schema': {
                                    'fields': source_schema
                                    },
                            'destinationTable': {
                                    'projectId': projectId,
                                    'datasetId': datasetId,
                                    'tableId': tableId
                                    },
                            }
                    }
            }

    return service.jobs().insert(
        projectId=projectId,
        body=job_data).execute(num_retries=num_retries)
# [END load_table]


# [START main]
def main():
    service = get_service()
    projectId = raw_input("Choose your project ID: ")
    datasetId = raw_input("Choose a dataset ID: ")
    tableId = raw_input("Choose a destination table name: ")

    schema_file_path = raw_input(
            "Enter the path to your table schema: ")
    with open(schema_file_path, 'r') as schema_file:
        schema = json.load(schema_file)

    data_file_path = raw_input(
            "Enter the Cloud Storage path for your csv file: ")

    job = load_table(service, schema, data_file_path,
                     projectId, datasetId, tableId)

    poll_job(service, **job['jobReference'])
# [END main]

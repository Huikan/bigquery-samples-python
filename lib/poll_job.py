import time

def poll_job(service, job_resource, timeout, max_timeout):
    job_collection = service.jobs()
   #[ START poll_job]
    job_status = job_resource['status']['state']
    while not job_status is 'DONE' and timeout<max_timeout:
        project_id = job_resource['jobReference']['projectId']
        job_id = job_resource['jobReference']['jobId']
        job_status = job_resource['status']['state']

        job_resource = job_collection.get(
            projectId=project_id,
            jobId=job_id).execute()
        print 'Waiting'+timeout+'seconds for export to complete..'
        time.sleep(timeout)
        timeout=timeout*2
    #[ END poll_job ]


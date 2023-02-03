
"""Zowe Python SDK z/OS Jobs Object Workshop."""
from zowe.zos_jobs_for_zowe_sdk import Jobs
from zowe.core_for_zowe_sdk import ProfileManager

from utils.pprint import pprint

profile = ProfileManager().load(profile_type='zosmf')
jobs = Jobs(profile)

"""Executing submit_from_mainframe method should submit the selected job and and return its status."""
output = jobs.submit_from_mainframe('IBMUSER.LIB.TEST(MEMBER2)')
pprint(*output.items(), sep='\n')

"""Executing get_jobs_status method should return the status of the selected job."""
jobname = output['jobname']
jobid = output['jobid']
output = jobs.get_job_status(jobname, jobid)
pprint(*output.items(), sep='\n')

"""Executing list_jobs method should return the list of job of the selected owner."""
owner = output['owner']
output = jobs.list_jobs(owner=owner)
for joblisting in output:
    pprint(*joblisting.items(), sep='\n')

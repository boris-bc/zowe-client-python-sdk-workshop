"""Zowe Python SDK z/OS Console Object Workshop."""

from zowe.zos_console_for_zowe_sdk import Console
from zowe.core_for_zowe_sdk import ProfileManager

from utils.pprint import pprint


# profile = {
#     "host": "example.com",
#     "port": 443,
#     "user": "<user>",
#     "password": "<password>"
# }
profile = ProfileManager().load(profile_type='zosmf')
console = Console(profile)

"""The execution of the time command should return the current time"""
output = console.issue_command('D T')
pprint (output['cmd-response'])

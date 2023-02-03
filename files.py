"""Zowe Python SDK z/OS Files Object Workshop."""

from zowe.zos_files_for_zowe_sdk import Files
from zowe.core_for_zowe_sdk import ProfileManager

from utils.pprint import pprint

profile = ProfileManager().load(profile_type='zosmf')
files = Files(profile)

"""Executing list_dsn method should return a list of found datasets."""
output = files.list_dsn('IBMUSER')
pprint (*output['items'], sep='\n')

"""Executing list_dsn_members should return a list of members."""
output = files.list_dsn_members('IBMUSER.LIB.TEST')
pprint (*output, sep='\n')

"""Executing get_dsn_content should return content from dataset."""
output = files.get_dsn_content('IBMUSER.LIB.TEST(MEMBER2)')
pprint (output['response'])

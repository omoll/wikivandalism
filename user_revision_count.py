from wkv_common import *

def user_revision_count(username):
    """actual feature, connects to wikpedia"""
    req = construct_user_page_edits_request(username,500)
    return len(get_user_page_revisions(make_wikipedia_request(req)))

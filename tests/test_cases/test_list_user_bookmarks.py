#
# This file is auto-generated, do not edit
#

from tests.test_cases.list_user_interactions import ListUserInteractionsTest
from recombee_api_client.api_requests import *

class ListUserBookmarksTestCase (ListUserInteractionsTest):

    def create_request(self, user_id):
        return ListUserBookmarks(user_id)
# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.22.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gitea
from gitea.api.notification_api import NotificationApi  # noqa: E501
from gitea.rest import ApiException


class TestNotificationApi(unittest.TestCase):
    """NotificationApi unit test stubs"""

    def setUp(self):
        self.api = NotificationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_notify_get_list(self):
        """Test case for notify_get_list

        List users's notification threads  # noqa: E501
        """
        pass

    def test_notify_get_repo_list(self):
        """Test case for notify_get_repo_list

        List users's notification threads on a specific repo  # noqa: E501
        """
        pass

    def test_notify_get_thread(self):
        """Test case for notify_get_thread

        Get notification thread by ID  # noqa: E501
        """
        pass

    def test_notify_new_available(self):
        """Test case for notify_new_available

        Check if unread notifications exist  # noqa: E501
        """
        pass

    def test_notify_read_list(self):
        """Test case for notify_read_list

        Mark notification threads as read, pinned or unread  # noqa: E501
        """
        pass

    def test_notify_read_repo_list(self):
        """Test case for notify_read_repo_list

        Mark notification threads as read, pinned or unread on a specific repo  # noqa: E501
        """
        pass

    def test_notify_read_thread(self):
        """Test case for notify_read_thread

        Mark notification thread as read by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

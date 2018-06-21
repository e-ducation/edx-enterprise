# -*- coding: utf-8 -*-

"""
X-API Client to send payload data.
"""
from __future__ import absolute_import, unicode_literals

import logging

from tincan import RemoteLRS

LOGGER = logging.getLogger(__name__)


class EnterpriseXAPIClient(object):
    """
    X-API to send payload data and handle responses.
    """

    def __init__(self, lrs_configuration):
        """
        Initialize X-API client.

        Arguments:
             lrs_configuration (XAPILRSConfiguration): Configuration object for X-API LRS.
        """

        self.lrs_configuration = lrs_configuration

    @property
    def lrs(self):
        """
        LRS client instance to be used for sending statements.
        """
        return RemoteLRS(
            version=self.lrs_configuration.version,
            endpoint=self.lrs_configuration.endpoint,
            auth=self.lrs_configuration.authorization_header,
        )

    def save_statement(self, statement):
        """
        Save X-API statement.

        Arguments:
            statement (EnterpriseStatement): X-API Statement to send to the LRS.
        """
        response = self.lrs.save_statement(statement)

        if not response:
            LOGGER.error("Statement failed to save.")

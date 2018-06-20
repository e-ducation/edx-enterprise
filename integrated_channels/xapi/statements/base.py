# -*- coding: utf-8 -*-

"""
Statements base for X-API.
"""
from __future__ import absolute_import, unicode_literals

from tincan.statement import Statement


class EnterpriseStatement(Statement):
    """
    Base statement for enterprise events.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize X-API statement.
        """
        super(EnterpriseStatement, self).__init__(*args, **kwargs)

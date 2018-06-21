# -*- coding: utf-8 -*-

"""
Models for X-API.
"""
from __future__ import absolute_import, unicode_literals

import base64

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from enterprise.models import EnterpriseCustomer


class XAPILRSConfiguration(TimeStampedModel):
    """
    X-API LRS configurations.
    """

    enterprise_customer = models.OneToOneField(
        EnterpriseCustomer,
        blank=False,
        null=False,
        help_text=_("Enterprise Customer associated with the configuration."),
    )
    version = models.CharField(max_length=16, default='1.0.1', help_text=_("Version of X-API."))
    endpoint = models.URLField(help_text=_('URL of the LRS.'))
    key = models.CharField(max_length=255, verbose_name="Client ID", help_text=_("Key of X-API LRS."))
    secret = models.CharField(max_length=255, verbose_name="Client Secret", help_text=_("secret of X-API LRS."))
    active = models.BooleanField(
        blank=False,
        null=False,
        help_text=_("Is this configuration active?"),
    )

    class Meta:
        app_label = 'xapi'

    def __str__(self):
        """
        Return human-readable string representation.
        """
        return "<XAPILRSConfiguration for Enterprise {enterprise_name}>".format(
            enterprise_name=self.enterprise_customer.name
        )

    def __repr__(self):
        """
        Return uniquely identifying string representation.
        """
        return self.__str__()

    @property
    def authorization_header(self):
        """
        Authorization header for authenticating requests to LRS.
        """
        return 'Basic {}'.format(
            base64.b64encode('{key}:{secret}'.format(key=self.key, secret=self.secret).encode()).decode()
        )

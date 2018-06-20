# -*- coding: utf-8 -*-
"""
Django admin integration for configuring sap_success_factors app to communicate with SAP SuccessFactors systems.
"""
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from integrated_channels.xapi.models import (
    XAPILRSConfiguration
)


@admin.register(XAPILRSConfiguration)
class XAPILRSConfigurationAdmin(admin.ModelAdmin):
    """
    Django admin model for SAPSuccessFactorsGlobalConfiguration.
    """
    fields = (
        'enterprise_customer',
        'active',
        'endpoint',
        'version',
        'key',
        'secret',
    )

    list_display = (
        'enterprise_customer_name',
        'active',
        'endpoint',
        'modified',
    )
    ordering = ('enterprise_customer__name', )
    list_filter = ('active', )
    search_fields = ('enterprise_customer__name',)

    class Meta(object):
        model = XAPILRSConfiguration

    def enterprise_customer_name(self, obj):
        """
        Returns: the name for the attached EnterpriseCustomer.

        Args:
            obj: The instance of XAPILRSConfiguration
                being rendered with this admin form.
        """
        return obj.enterprise_customer.name

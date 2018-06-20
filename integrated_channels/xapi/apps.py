# -*- coding: utf-8 -*-
"""
Enterprise X-API Django application initialization.
"""
from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig


class XAPIConfig(AppConfig):
    """
    Configuration for the X-API Django application.
    """
    name = 'integrated_channels.xapi'
    verbose_name = "Enterprise X-API Integration"

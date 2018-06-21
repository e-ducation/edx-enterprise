# -*- coding: utf-8 -*-

"""
Utility functions for X-API.
"""

from __future__ import absolute_import, unicode_literals

from integrated_channels.xapi.client import EnterpriseXAPIClient
from integrated_channels.xapi.statements.learner_course_enrollment import LearnerCourseEnrollmentStatement


def send_xapi_statement_course_enrollment(lrs_configuration, course_enrollment):
    """
    Send X-API statement for course enrollment.

    Arguments:
         lrs_configuration (XAPILRSConfiguration): XAPILRSConfiguration instance where to send statements.
         course_enrollment (CourseEnrollment): Course enrollment object.
    """
    statement = LearnerCourseEnrollmentStatement(course_enrollment.user, course_enrollment.course, {}, {})
    EnterpriseXAPIClient(lrs_configuration).save_statement(statement)

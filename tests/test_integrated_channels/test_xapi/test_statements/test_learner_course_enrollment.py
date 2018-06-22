# -*- coding: utf-8 -*-
"""
Test for X-API Learner Course Enrollment Statements.
"""

from __future__ import absolute_import, unicode_literals

import json
import unittest

from faker import Factory as FakerFactory
from mock import Mock
from pytest import mark

from integrated_channels.xapi.statements.learner_course_enrollment import LearnerCourseEnrollmentStatement
from test_utils import factories


@mark.django_db
class TestLearnerCourseEnrollmentStatement(unittest.TestCase):
    """
    Tests for the ``LearnerCourseEnrollmentStatement`` model.
    """

    def setUp(self):
        super(TestLearnerCourseEnrollmentStatement, self).setUp()
        faker = FakerFactory.create()

        self.user = factories.UserFactory()
        # pylint: disable=no-member
        self.course_overview = Mock(display_name=faker.text(max_nb_chars=25), short_description=faker.text())

        self.expected = {
            "verb":
                {
                    "id": "http://adlnet.gov/expapi/verbs/registered",
                    "display": {"en-US": "registered"}
                },
            "version": "1.0.1",
            "actor":
                {
                    "mbox": "mailto:{email}".format(email=self.user.email),
                    "name": self.user.username,
                    "objectType": "Agent"
                },
            "object":
                {
                    "definition":
                        {
                            "description":
                                {
                                    "en-US": self.course_overview.short_description
                                },
                            "name":
                                {
                                    "en-US": self.course_overview.display_name
                                }
                        },
                    "id": "http://adlnet.gov/expapi/activities/course",
                    "objectType": "Activity"
                }
        }

    def test_statement(self):
        """
        Validate statement when learner enrolls in a course.
        """
        statement = LearnerCourseEnrollmentStatement(self.user, self.course_overview)
        assert json.loads(statement.to_json()) == self.expected

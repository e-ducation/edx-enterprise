# -*- coding: utf-8 -*-

"""
X API Statement when learner enrolls in a course.
"""
from __future__ import absolute_import, unicode_literals

from tincan import Agent, Context, Verb, LanguageMap, Activity, ActivityDefinition

from integrated_channels.xapi.statements.base import EnterpriseStatement


class LearnerCourseEnrollmentStatement(EnterpriseStatement):
    """
    X-API Statement to serialize data related to course registration.
    """

    def __init__(self, user, course_overview, user_details, course_details, *args, **kwargs):
        """
        Initialize and populate statement with learner info and course info.

        Arguments:
            user (User): Auth User object containing information about the learner enrolling in the course.
            course_overview (CourseOverview): course overview object containing course details.
            user_details (dict): A dict object containing learner info we want to send in X-API statement payload.
            course_details (dict): A dict object containing course info we want to send in X-API statement payload.
        """
        kwargs.update(
            actor=self.get_actor(user.username, user.email),
            verb=self.get_verb(),
            object=self.get_object(course_overview.display_name, course_overview.short_description),
        )
        super(LearnerCourseEnrollmentStatement, self).__init__(*args, **kwargs)

    def get_actor(self, username, email):
        """
        Get actor for course enrollment statement.
        """
        return Agent(
                name=username,
                mbox='mailto:{email}'.format(email=email),
            )

    def get_verb(self):
        """
        Get verb for course enrollment statement.
        """
        return Verb(
            id='http://adlnet.gov/expapi/verbs/registered',
            display=LanguageMap({'en-US': 'registered'}),
        )

    def get_object(self, name, description):
        """
        Get verb for course enrollment statement.
        """
        return Activity(
            id='http://adlnet.gov/expapi/activities/course',
            definition=ActivityDefinition(
                name=LanguageMap({'en-US': name}),
                description=LanguageMap({'en-US': description}),
            ),
        )

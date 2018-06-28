# -*- coding: utf-8 -*-

"""
xAPI statement for course completion.
"""
from __future__ import absolute_import, unicode_literals

from tincan import Activity, ActivityDefinition, Agent, Context, Extensions, LanguageMap, Result, Score, Verb

from integrated_channels.xapi.statements.base import EnterpriseStatement


class LearnerCourseCompletionStatement(EnterpriseStatement):
    """
    xAPI Statement to serialize data related to course completion.
    """

    def __init__(self, user, course_overview, user_details, course_details, course_grade, *args, **kwargs):
        """
        Initialize and populate statement with learner info and course info.

        Arguments:
            user (User): Auth User object containing information about the learner enrolling in the course.
            course_overview (CourseOverview): course overview object containing course details.
            user_details (dict): A dict object containing learner info we want to send in xAPI statement payload.
            course_details (dict): A dict object containing course info we want to send in xAPI statement payload.
            course_grade (CourseGrade): User grade in the course.
        """
        kwargs.update(
            actor=self.get_actor(user.username, user.email),
            verb=self.get_verb(),
            object=self.get_object(course_overview.display_name, course_overview.short_description),
            result=self.get_result(course_grade),
            context=self.get_context(user_details, course_details)
        )
        super(LearnerCourseCompletionStatement, self).__init__(*args, **kwargs)

    def get_actor(self, username, email):
        """
        Get actor for the statement.
        """
        return Agent(
            name=username,
            mbox='mailto:{email}'.format(email=email),
        )

    def get_verb(self):
        """
        Get verb for the statement.
        """
        return Verb(
            id='http://adlnet.gov/expapi/verbs/completed',
            display=LanguageMap({'en-US': 'completed'}),
        )

    def get_object(self, name, description):
        """
        Get verb for the statement.
        """
        return Activity(
            id='http://adlnet.gov/expapi/activities/course',
            definition=ActivityDefinition(
                name=LanguageMap({'en-US': name}),
                description=LanguageMap({'en-US': description}),
            ),
        )

    def get_result(self, course_grade):
        """
        Get result for the statement.

        Arguments:
            course_grade (CourseGrade): Course grade.
        """
        return Result(
            score=Score(
                scaled=course_grade.percent,
                raw=course_grade.percent * 100,
                min=0,
                max=100,
            ),
            success=course_grade.passed,
            completion=course_grade.passed,
            duration=None,  # should be a datetime.timedelta object.
        )

    def get_context(self, user_details, course_details):
        """
        Get verb for the statement.
        """
        return Context(
            extensions=Extensions(
                {
                    'http://id.tincanapi.com/extension/user-details': user_details,
                    'http://id.tincanapi.com/extension/course-details': course_details,
                },
            )
        )

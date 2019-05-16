from sentry.plugins import Plugin


class RegressionPlugin(Plugin):

    def is_regression(self, group, event, **kwargs):
        """
        Called on new events when the group's status is resolved.
        Return True if this event is a regression, False if it is not,
        None to defer to other plugins.

        :param group: an instance of ``Group``
        :param event: an instance of ``Event``
        """
        return None

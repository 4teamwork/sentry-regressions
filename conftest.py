from __future__ import absolute_import

from django.conf import settings
import os

pytest_plugins = ['sentry.utils.pytest']

# See https://github.com/getsentry/sentry/blob/9.1.0/src
# /sentry/utils/pytest/sentry.py#L39-L72
os.environ.setdefault('DB', 'sqlite')


def pytest_configure(config):
    # Sentry's pytest plugin explicitly doesn't load plugins, so let's load all of them
    # and ignore the fact that we're not *just* testing our own
    # Note: We could manually register/configure INSTALLED_APPS by traversing our entry points
    # or package directories, but this is easier assuming Sentry doesn't change APIs.
    # Note: Order of operations matters here.
    from sentry.runner.importer import install_plugin_apps
    install_plugin_apps('sentry.apps', settings)

    from sentry.runner.initializer import register_plugins
    register_plugins(settings)

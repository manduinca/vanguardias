# -*- coding: utf-8 -*-

import os

from django.core.exceptions import ImproperlyConfigured


def get_var(key, default=None):  # Added to help use env variables
    """Retrieves system enviroment variable or makes value replacements

        Returns:
            default: any value if it doesn't exist.

        Raises:
            ImproperlyConfigured: if `key` hasn't been found
    """
    val = os.environ.get(key, default)
    if not val:
        error_msg = "Set the %s env variable" % key
        raise ImproperlyConfigured(error_msg)

    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val


try:
    from vanguardias.local_system import get_var
except ImportError:
    pass

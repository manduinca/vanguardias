# -*- coding: utf-8 -*-

from apps.customuser import strings as customuser_strings

WRITER_TYPE = 1
ADMIN_TYPE = 2

USER_TYPE = (
    (WRITER_TYPE, customuser_strings.WRITER_TYPE),
    (ADMIN_TYPE, customuser_strings.ADMIN_TYPE)
)

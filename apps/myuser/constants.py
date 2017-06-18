# -*- coding: utf-8 -*-

from apps.myuser import strings as customuser_strings

WRITER_TYPE = 1
ADMIN_TYPE = 2
MEMBER_TYPE = 3

USER_TYPE = (
    (WRITER_TYPE, customuser_strings.WRITER_TYPE),
    (ADMIN_TYPE, customuser_strings.ADMIN_TYPE),
    (MEMBER_TYPE, customuser_strings.MEMBER_TYPE)
)

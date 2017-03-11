# coding=utf-8

import xadmin

from .. import models

class AAdmin(object):
    list_display = ('name', 'b', 'ename')
    pass
xadmin.site.register(models.A, AAdmin)
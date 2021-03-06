from __future__ import division
__author__ = u'schmatz'

import sys
import os
from errors import NotSupportedError
class SystemConfiguration(object):

    def __init__(self):
        self.operating_system = self.get_operating_system()
        self.virtual_memory_address_width = self.get_virtual_memory_address_width()

    def get_operating_system(self):
        platform = sys.platform
        if platform.startswith(u'linux'):
            return u"linux"
        elif platform.startswith(u'darwin'):
            return u"mac"
        elif platform.startswith(u'win'):
            return u"windows"
        else:
            raise NotSupportedError(u"Your platform," + sys.platform + u",isn't supported.")

    def get_current_working_directory(self):
        return os.getcwdu()

    def get_virtual_memory_address_width(self):
        is64Bit = sys.maxsize/3 > 2**32
        if is64Bit:
            return 64
        else:
            if self.operating_system == u"mac":
                raise NotSupportedError(u"Your processor is determined to have a maxSize of" + sys.maxsize +
                                        u",\n which doesn't correspond with a 64-bit architecture.")
            return 32


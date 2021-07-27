import cgitb
import datetime

import sys

import eliot

from markupsafe import Markup
from ekklesia_common.debug.tbtools import Traceback

from ekklesia_portal.concepts.ekklesia_portal.cell.layout import LayoutCell


class ExceptionCell(LayoutCell):

    model_properties = ["task_uuid"]

    @property
    def is_global_admin(self):
        return self._request.current_user and self._request.identity.has_global_admin_permissions

    def show_exception_details(self):
        return self.is_global_admin

    def xid(self):
        import traceback
        import hashlib
        import random
        import string
        """Builds a unique string (exception ID) that may be exposed to the user without revealing to much.
        Added to the logging of an event should make it easier to relate.

        :param errormsg: str
        """
        # : and - interferes with elasticsearch query syntax, better use underscores in the datetime string
        date_now = datetime.datetime.now().strftime("%Y_%m_%dT%H_%M_%S")
        exc = self._model.__cause__
        error_msg = str(exc)
        formatted_traceback = "\n".join(traceback.format_tb(exc.__traceback__))
        hashed_errormsg = hashlib.md5(error_msg.encode("utf8")).hexdigest()[:6]
        hashed_tb = hashlib.md5(formatted_traceback.encode("utf8")).hexdigest()[:6]
        # http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
        random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        xid = "%s__%s__%s__%s" % (date_now, hashed_tb, hashed_errormsg, random_string)
        return xid

    def traceback(self):
        if self.is_global_admin:
            exc = self._model.__cause__
            werkzeug_traceback = Traceback(exc.__class__, exc, exc.__traceback__)
            return Markup(werkzeug_traceback.render_full())

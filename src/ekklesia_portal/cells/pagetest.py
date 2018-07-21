from markupsafe import Markup

from ekklesia_portal.cells.layout import LayoutCell
from ekklesia_portal.helper.cell import Cell


class PageTestCell(LayoutCell):
    test_str = "test"
    test_int = 42
    test_url = "http://example.com"
    test_escaped_html = "<div>HTML from the cell (div should be escaped)</div>"
    test_html = Markup("<div>HTML from the cell (div should not be escaped)</div>")


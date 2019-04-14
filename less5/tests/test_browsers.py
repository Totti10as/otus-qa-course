""" Tests scripts"""


def test_pagetitle(selectbrowser, request):
    """
    Running test script
    """
    selectbrowser.get("".join([request.config.getoption("--address")]))
    page_title = selectbrowser.title
    assert page_title == 'Your Store'

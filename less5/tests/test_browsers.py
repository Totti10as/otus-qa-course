""" Tests scripts"""
def test_pagetitle(selectbrowser, base_url):
    """
    Running test script
    """
    selectbrowser.get(base_url)
    page_title = selectbrowser.title
    assert page_title == 'Your Store'

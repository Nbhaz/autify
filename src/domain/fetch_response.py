class FetchResponse:

    def __init__(self, is_success: bool, content: str = None, error: str = None):
        self._success = is_success
        self._content = content
        self._error = error

    def is_success(self):
        return self._success

    def get_content(self):
        return self._content

    def get_error(self):
        return self._error

class WorkNumberConverter:
    regex = "[0-9]{1,2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

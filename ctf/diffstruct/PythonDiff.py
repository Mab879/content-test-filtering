from ctf.diffstruct.AbstractDiffStruct import AbstractDiffStruct
from ctf.constants import FileType


class PythonDiffStruct(AbstractDiffStruct):
    def __init__(self, absolute_path):
        super().__init__(absolute_path)
        self.file_type = FileType.PYTHON
        self.changed = False

    def fill_tests(self, tests):
        if self.changed:
            tests.add_python_test(self.absolute_path)
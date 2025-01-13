
from west.commands import WestCommand  # your extension must subclass this
from west import log                   # use this for user output
import subprocess

class Clean(WestCommand):
    def __init__(self):
        super().__init__(
            'clean',               # gets stored as self.name
            'Clean all generated files',  # self.help
            ""
        )
        self.build_dirs = ("src-gen", "build")

    def do_add_parser(self, parser_adder):
        parser = parser_adder.add_parser(self.name,
                                         help=self.help,
                                         description=self.description)
        return parser           # gets stored as self.parser

    def clean_directory(self, dir):
        res = subprocess.Popen(f"rm -rf {dir}", shell=True)
        ret = res.wait()
        if ret != 0:
            exit(1)

    def do_run(self, args, unknown_args):
        log.inf(f"Removing all generated files in {self.build_dirs}")
        for d in self.build_dirs:
            self.clean_directory(d)


from west.commands import WestCommand  # your extension must subclass this
from west import log                   # use this for user output

import os
import shutil
import subprocess

class GenFedTemplate(WestCommand):
    def __init__(self):
        super().__init__(
            'gen_fed_template',
            'Generate a zephyr project template for a Lingua Franca federate.',
            ""
        )
    def do_add_parser(self, parser_adder):
        parser = parser_adder.add_parser(self.name,
                                         help=self.help,
                                         description=self.description)

        parser.add_argument('--lf-main', type=str, required=True, help='Name of LF Main file')
        parser.add_argument('--federate', type=str, required=True, help='Name of federate')
        parser.add_argument('-o', '--output', type=str, help='Output directory')

        return parser           # gets stored as self.parser

    def do_run(self, args, unknown_args):
        self.args = args
        # Check if the output directory exists
        if args.output:
            self.output_path = os.path.join(os.path.join(os.getcwd(), args.output), args.federate)
        else:
            self.output_path = os.path.join(os.getcwd(), args.federate)
        
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path, exist_ok=True)

        # Calculate relative path back to the project root
        self.project_root = os.getcwd()
        self.output_path_abs = os.path.abspath(self.output_path)
        self.rel_path_to_root = os.path.relpath(self.project_root, self.output_path_abs)

        # Write CMakeLists.txt
        with open(f"{self.output_path}/CMakeLists.txt", "w") as f:
            f.write(self.generate_cmakelists())
        
        # Write prj.conf
        with open(f"{self.output_path}/prj.conf", "w") as f:
            f.write(self.generate_prj_conf())
        
            
    def generate_cmakelists(self):
        return f"""
cmake_minimum_required(VERSION 3.20.0)

set(PLATFORM "ZEPHYR" CACHE STRING "Platform to target")
set(BOARD "native_sim")
set(LF_MAIN {self.args.lf_main})
set(PROJECT_ROOT ${{CMAKE_CURRENT_SOURCE_DIR}}/{self.rel_path_to_root})
set(FEDERATE {self.args.federate})
find_package(Zephyr REQUIRED HINTS ${{PROJECT_ROOT}}/deps/zephyr)
project({self.args.federate})

include($ENV{{REACTOR_UC_PATH}}/cmake/lfc.cmake)
lf_setup()
lf_run_lfc(${{PROJECT_ROOT}}/src ${{LF_MAIN}})
lf_build_generated_code(app ${{CMAKE_CURRENT_SOURCE_DIR}}/src-gen/${{LF_MAIN}}/${{FEDERATE}})
        """
    
    def generate_prj_conf(self):
        return """
CONFIG_ETH_NATIVE_POSIX=n
CONFIG_NET_DRIVERS=y
CONFIG_NETWORKING=y
CONFIG_NET_TCP=y
CONFIG_NET_IPV4=y
CONFIG_NET_SOCKETS=y
CONFIG_POSIX_API=y
CONFIG_ASSERT=y
CONFIG_MAIN_STACK_SIZE=16384
CONFIG_HEAP_MEM_POOL_SIZE=1024

# Network address config
CONFIG_NET_CONFIG_SETTINGS=y
CONFIG_NET_CONFIG_NEED_IPV4=y
CONFIG_NET_CONFIG_MY_IPV4_ADDR="127.0.0.1"

CONFIG_NET_SOCKETS_OFFLOAD=y
CONFIG_NET_NATIVE_OFFLOADED_SOCKETS=y
        """
        
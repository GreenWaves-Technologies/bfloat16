import os
import sys
import shutil
from distutils.command.build_ext import build_ext
from distutils.core import Extension, setup
from distutils.sysconfig import customize_compiler

PACKAGE_NAME='bfloat16'

import numpy as np

if 'clean' in sys.argv:
    curdir = os.path.dirname(os.path.realpath(__file__))
    for filepath in ['build', 'dist', f'{PACKAGE_NAME}.egg-info', 'MANIFEST']:
        if os.path.exists(filepath):
            if os.path.isfile(filepath):
                os.remove(filepath)
            else:
                shutil.rmtree(filepath)

class my_build_ext(build_ext):
    def build_extensions(self):
        customize_compiler(self.compiler)
        try:
            self.compiler.compiler_so.remove("-Wstrict-prototypes")
        except (AttributeError, ValueError):
            pass
        build_ext.build_extensions(self)


module1 = Extension(PACKAGE_NAME,
                    sources=['bfloat16.cc'],
                    include_dirs=[np.get_include()])

setup(name=PACKAGE_NAME,
      version='1.0',
      description='Numpy bfloat16 package',
      ext_modules=[module1],
      cmdclass={'build_ext': my_build_ext})

#!/usr/bin/env python
#! coding: utf-8

import os
import sys
import platform
import subprocess
from distutils.core import setup, Extension

# avoid building universal binary (ppc) on osx non-ppc platforms
if sys.platform == 'darwin':
    arch = platform.machine()
    if arch in ('i386', 'x86_64'):
        os.environ['ARCHFLAGS'] = '-arch i386 -arch x86_64'

extra_compile_args = ['-g', '-fPIC', '-Wall', '-O2']

VERSION = '0.1.3'

if not os.path.exists('smhasher/src'):
    sys.stderr.write('run command:\ngit submodule update --init\n')
    p = subprocess.Popen(args=['git','submodule','update','--init'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outs, errs = p.communicate()
    p.wait()
    sys.stderr.write(outs)
    sys.stderr.write(errs)

cpp_files = [
    'smhasher/src/MurmurHash2.cpp',
    'smhasher/src/MurmurHash3.cpp',
    'pysmhasher.cpp'
]

pysmhasher_ext = Extension(
    'pysmhasher',
    sources=cpp_files,
    include_dirs=['smhasher/src'],
    define_macros=[('MODULE_VERSION', '"{}"'.format(VERSION))],
    extra_compile_args=extra_compile_args
)

setup(
    name='pysmhasher',
    version=VERSION,
    maintainer='Yong Li',
    maintainer_email='liyong19861014@gmail.com',
    url='https://github.com/airhuman/pysmhasher.git',
    description='Python Extensions for SMHasher',
    keywords=['hash', 'smhasher'],
    ext_modules=[pysmhasher_ext]
)

#!/usr/bin/env python
#! coding: utf-8

import os
import sys
import io
import platform
import subprocess
from setuptools import setup, Extension

# avoid building universal binary (ppc) on osx non-ppc platforms
if sys.platform == 'darwin':
    arch = platform.machine()
    if arch in ('i386', 'x86_64'):
        os.environ['ARCHFLAGS'] = '-arch i386 -arch x86_64'

extra_compile_args = ['-g', '-fPIC', '-Wall', '-O2']

VERSION = '0.1.9'

if not os.path.exists('smhasher/src'):
    sys.stderr.write('run command:\ngit submodule update --init\n')
    p = subprocess.Popen(args=['git', 'submodule', 'update', '--init'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outs, errs = p.communicate()
    p.wait()
    sys.stderr.write(outs)
    sys.stderr.write(errs)

here = os.path.abspath(os.path.dirname(__file__))

readme = os.path.join(here, 'README.rst')
try:
    long_description = io.open(readme, mode='r', encoding='utf-8').read()
except (IOError, ImportError):
    long_description = ''  # never got here

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
    author='Yong Li',
    author_email='liyong19861014@gmail.com',
    url='https://github.com/airhuman/pysmhasher.git',
    description='Python Extensions for SMHasher',
    long_description=long_description,
    keywords='hash hashing smhasher',
    license='MIT',
    ext_modules=[pysmhasher_ext],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

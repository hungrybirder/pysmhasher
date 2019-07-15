Google SMHasher Python 扩展
===========================

[![Build Status](https://travis-ci.org/hungrybirder/pysmhasher.svg?branch=master)](https://travis-ci.org/hungrybirder/pysmhasher)
[![PyPI](https://img.shields.io/pypi/v/pysmhasher.svg)](https://pypi.python.org/pypi/pysmhasher)
![](https://img.shields.io/pypi/pyversions/pysmhasher.svg)
![](https://img.shields.io/pypi/l/pysmhasher.svg)

pysmhasher封装SMHasher中，更多的方法

使用方法
--------

```
#从pip源安装
pip install pysmhasher

#调用方法
>>> import pysmhasher
>>> pysmhasher.murmurhash2('hello')
3848350155
>>> seed = 27
>>> pysmhasher.murmurhash2('hello', seed)
1143501851

>>> pysmhasher.cityhash64("DBE4CBA7-2ADC-4F32-8D54-D8F065FED9CC")
6587470800993669582

#下载代码并安装
git clone --recurse-submodules https://github.com/hungrybirder/pysmhasher.git
cd pysmhasher
python setup.py install
```

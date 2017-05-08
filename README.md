Google SMHasher Python 扩展
===========================

pysmhasher封装SMHasher中，更多的方法

License: MIT License


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

#下载代码并安装
git clone --recurse-submodules https://github.com/airhuman/pysmhasher.git
cd pysmhasher
python setup.py install
```

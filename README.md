# Google SMHasher Python 扩展 #

参考[python-smhasher](https://github.com/phensley/python-smhasher)

提供SMHasher中，更多的方法

License: MIT License


## 从pypi上安装 ##
```
pip install pysmhasher
```

## 使用方法 ##
```
>>> import pysmhasher
>>> pysmhasher.murmurhash2('hello')
3848350155
>>> seed = 27
>>> pysmhasher.murmurhash2('hello', seed)
1143501851
```

## 下载代码并安装 ##
```
git clone --recurse-submodules https://github.com/airhuman/pysmhasher.git
cd pysmhasher
python setup.py install
```



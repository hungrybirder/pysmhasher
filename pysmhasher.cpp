#include <Python.h>
#include <stdint.h>

#include "MurmurHash2.h"
#include "MurmurHash3.h"

PyDoc_STRVAR(module_doc, "Python Extensions for SMHasher");

static PyObject *PY_MurmurHash2(PyObject *self, PyObject *args) {
  char *key;
  unsigned len;
  unsigned seed = 0;
  if (!PyArg_ParseTuple(args, "s#|I", &key, &len, &seed)) {
    return NULL;
  }
  uint32_t h = MurmurHash2(key, len, seed);
  return PyLong_FromUnsignedLong(h);
}

static PyObject *PY_MurmurHash2A(PyObject *self, PyObject *args) {
  char *key;
  unsigned len;
  unsigned seed = 0;
  if (!PyArg_ParseTuple(args, "s#|I", &key, &len, &seed)) {
    return NULL;
  }
  uint32_t h = MurmurHash2A(key, len, seed);
  return PyLong_FromUnsignedLong(h);
  return PyLong_FromUnsignedLongLong(h);
}

static PyObject *PY_MurmurHash64B(PyObject *self, PyObject *args) {
  char *key;
  unsigned len;
  unsigned seed = 0;
  if (!PyArg_ParseTuple(args, "s#|I", &key, &len, &seed)) {
    return NULL;
  }
  uint64_t h = MurmurHash64B(key, len, seed);
#if defined(__x86_64__)
  return PyLong_FromUnsignedLong(h);
#else
  return PyLong_FromUnsignedLongLong(h);
#endif
}

static PyObject *PY_MurmurHash3_x86_32(PyObject *self, PyObject *args) {
  const char *key;
  Py_ssize_t len;
  uint32_t seed = 0;
  unsigned char out[4];

  if (!PyArg_ParseTuple(args, "s#|I", &key, &len, &seed)) {
    return NULL;
  }
  MurmurHash3_x86_32((void *)key, len, seed, &out);
  return _PyLong_FromByteArray((const unsigned char *)&out, 4, 0, 0);
}

static PyObject *PY_MurmurHash3_x86_128(PyObject *self, PyObject *args) {
  const char *key;
  Py_ssize_t len;
  uint32_t seed = 0;
  unsigned char out[16];

  if (!PyArg_ParseTuple(args, "s#|I", &key, &len, &seed)) {
    return NULL;
  }
  MurmurHash3_x86_128((void *)key, len, seed, &out);
  return _PyLong_FromByteArray((const unsigned char *)&out, 16, 0, 0);
}

// 32-bit end

// 64-bit
#if defined(__x86_64__)
static PyObject *PY_MurmurHash64A(PyObject *self, PyObject *args) {
  char *key;
  unsigned len;
  unsigned seed = 0;
  if (!PyArg_ParseTuple(args, "s#|I", &key, &len, &seed)) {
    return NULL;
  }
  uint64_t h = MurmurHash64A(key, len, seed);
  return PyLong_FromUnsignedLong(h);
}

static PyObject *PY_MurmurHash3_x64_128(PyObject *self, PyObject *args) {
  const char *key;
  Py_ssize_t len;
  uint32_t seed = 0;
  unsigned char out[16];

  if (!PyArg_ParseTuple(args, "s#|I", &key, &len, &seed)) {
    return NULL;
  }
  MurmurHash3_x64_128((void *)key, len, seed, &out);
  return _PyLong_FromByteArray((const unsigned char *)&out, 16, 0, 0);
}
#endif

#if defined(__x86_64__)
static PyMethodDef methods[] = {
    {"murmurhash2", PY_MurmurHash2, METH_VARARGS, "32-bit hash"},
    {"murmurhash2A", PY_MurmurHash2A, METH_VARARGS,
     "32-bit hash, a variant of murmurhash2"},
    {"murmurhash64A", PY_MurmurHash64A, METH_VARARGS,
     "64-bit hash for 64-bit platform"},
    {"murmurhash64B", PY_MurmurHash64B, METH_VARARGS,
     "64-bit hash for 32-bit platform"},
    {"murmurhash3_x86_32", PY_MurmurHash3_x86_32, METH_VARARGS, "32-bit hash"},
    {"murmurhash3_x64_128", PY_MurmurHash3_x64_128, METH_VARARGS,
     "128-bit hash"},
    {NULL, NULL, 0, NULL}};  // sentinel
#else
static PyMethodDef methods[] = {
    {"murmurhash2", PY_MurmurHash2, METH_VARARGS, "32-bit hash"},
    {"murmurhash2A", PY_MurmurHash2A, METH_VARARGS,
     "32-bit hash, a variant of murmurhash2"},
    {"murmurhash64B", PY_MurmurHash64B, METH_VARARGS,
     "64-bit hash for 32-bit platform"},
    {"murmurhash3_x86_32", PY_MurmurHash3_x86_32, METH_VARARGS, "32-bit hash"},
    {"murmurhash3_x86_128", PY_MurmurHash3_x86_128, METH_VARARGS,
     "128-bit hash"},
    {NULL, NULL, 0, NULL}};  // sentinel

#endif

#if PY_MAJOR_VERSION == 3  // python3
static struct PyModuleDef pysmhasher_module = {
    PyModuleDef_HEAD_INIT, module_doc,
    "smhasher python extensions",  // doc
    -1, methods};

#ifdef __cplusplus
extern "C" {
#endif
PyMODINIT_FUNC PyInit_pysmhasher(void) {
  PyObject *m;

  m = PyModule_Create(&pysmhasher_module);
  PyModule_AddStringConstant(m, "__version__", MODULE_VERSION);
  return m;
}
#ifdef __cplusplus
}
#endif

#else  // python2

#ifdef __cplusplus
extern "C" {
#endif
PyMODINIT_FUNC initpysmhasher(void) {
  PyObject *m;

  m = Py_InitModule3("pysmhasher", methods, module_doc);
  PyModule_AddStringConstant(m, "__version__", MODULE_VERSION);
  return;
}
#ifdef __cplusplus
}
#endif

#endif

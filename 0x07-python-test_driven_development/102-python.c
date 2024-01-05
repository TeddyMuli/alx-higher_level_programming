#include "Python.h"

void print_python_string(PyObject *p)
{
    PyUnicodeObject *u_code = (PyUnicodeObject*) p;

    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(u_code) ? "str" : "u_code");
    printf("  length: %ld\n", PyUnicode_GetLength(p));
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
}

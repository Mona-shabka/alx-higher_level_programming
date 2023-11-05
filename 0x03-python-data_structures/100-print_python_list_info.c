#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - a function that  prints info about pytohn list.
* @p: python object.
**/

void print_python_list_info(PyObject *p)
{
	long int m_size = PyList_Size(p);
	int m;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", m_size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (m = 0; m < m_size; m++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}

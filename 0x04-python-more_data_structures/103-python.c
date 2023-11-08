#include <Python.h>
#include <stdio.h>


void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - a function that prints bytes information.
 * @p: Python Object.
 * Return: void.
 */

void print_python_bytes(PyObject *p)
{
	char *str;
	long int m, s, l;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyVarObject *)(p))->ob_string;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);
	if (s >= 10)
		l = 10;
	else
		l = s + 1;
	printf("  first %ld bytes:", l);
	for (m = 0; m < l; m++)
		if (str[m] >= 0)
			printf(" %02x", str[m]);
		else
			printf(" %02x", 256 + str[m]);
	printf("\n");
}

/**
 * print_python_list - a function that prints list information.
 * @p: Python Object.
 * Return: void.
 */

void print_python_list(PyObject *p)
{
	long int s, m;
	PyListObject *list;
	PyObject *obj;

	s = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (m = 0; m < s; m++)
	{
		obj = ((PyListObject *)p)->ob_item[m];
		printf("Element %ld: %s\n", m, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

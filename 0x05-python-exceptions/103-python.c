#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - a function to prints information about Python.
 * @p: Address of PyObject.
 * Return: avoid.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t m_alloc, m_size, m;
	const char *m_type;
	PyListObject *m_list = (PyListObject *)p;
	PyVarObject *m_var = (PyVarObject *)p;

	m_size = m_var->ob_size;
	m_alloc = m_list->allocated;
	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", m_size);
	printf("[*] Allocated = %ld\n", m_alloc);
	for (m = 0; m < m_size; m++)
	{
		m_type = m_list->ob_item[m]->ob_type->tp_name;
		printf("Element %ld: %s\n", m, m_type);
		if (strcmp(m_type, "bytes") == 0)
			print_python_bytes(m_list->ob_item[m]);
		else if (strcmp(m_type, "float") == 0)
			print_python_float(m_list->ob_item[m]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - A function that prints info about Python float.
 * @p: Address of PyObject float.
 */

void print_python_float(PyObject *p)
{
	PyFloatObject *float__obj = (PyFloatObject *)p;
	char *m_buffer = NULL;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	m_buffer = PyOS_double_to_string(float__obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", m_buffer);
	PyMem_Free(m_buffer);
}

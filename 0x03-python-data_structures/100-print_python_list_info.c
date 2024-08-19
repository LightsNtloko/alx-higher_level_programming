#include <Python.h>

/**
 * print_python_list_info - The function that prints basic information about
 * Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocate, k;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);

	allocate = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %zd\n", allocate);

	for (k = 0; k < size; k++)
	{
		PyObject *item = PyList_GetItem(p, k);
		printf("Element %zd: %s\n", k, Py_TYPE(item)->tp_name);
	}
}

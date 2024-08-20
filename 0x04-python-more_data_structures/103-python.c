#include <Python.h>
#include <stdio.h>

/* Function to print information about Python bytes objects */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	Py_ssize_t size = PyBytes_Size(p);
	const char *string = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string ? string : "(null)");

	printf("  first %zd bytes: ", size > 10 ? 10 : size);
	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf("%02x ", (unsigned char)string[i]);
	}
	printf("\n");
}

/* Function to print information about Python lists */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[.] Python list info\n");
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t n = 0; n < size; n++)
	{
		PyObject *item = PyList_GetItem(p, n);
		const char *type = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", n, type);
		if (strcmp(type, "bytes") == 0)
		{
			print_python_bytes(item);
		}
	}
}

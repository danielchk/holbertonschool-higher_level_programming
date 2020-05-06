#include <Python.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t sz, idx = 0;
	PyObject *object;
    
	struct _typeobject *format;

	if (strcmp(p->ob_type->tp_name, "list") == 0)
	{
		list = (PyListObject *)p;
		sz = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", sz);
		printf("[*] Allocated = %ld\n", list->allocated);
		while (idx < sz)
		{
			object = list->ob_item[idx];
			format = object->ob_type;
			printf("Element %ld: %s\n", idx, format->tp_name);
            idx++;
		}
	}
}
#include "search_algos.h"

/**
 * Function that searches for a value in an
 * array of integers using the Linear search algorithm
 * @array:pointer to the first element of the array to search
 * @size: number of elements in array
 * @value: number to search
 */

int linear_search(int *array, size_t size, int value)
{
    size_t i = 0;
    if(!array)
        return(-1);
    
    while (i < size)
    {
        printf("Value checked array[%lu] = [%i]\n", i, array[i]);
        if (array[i] == value)
            return (i);
        i++;
    }

}

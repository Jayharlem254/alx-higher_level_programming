#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct Node - Node of a linked list
 * @data: Data stored in the node
 * @next: Pointer to the next node in the list
 */
typedef struct Node
{
    int data;
    struct Node *next;
} Node;

/**
 * function_name - Brief description of the function
 * @param1: Description of the first parameter
 * @param2: Description of the second parameter
 * Return: Description of the return value
 */
void function_name(int param1, char param2);

/* Additional function prototypes go here */

#endif /* LISTS_H */


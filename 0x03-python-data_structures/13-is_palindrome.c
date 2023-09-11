#include <stddef.h>
#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
size_t length = 0;
int i = 0;
size_t j;
listint_t *current = *head;
int *list;
if (*head == NULL)
{
return (1);
}
while (current != NULL)
{
length++;
current = current->next;
}
list = (int *)malloc(sizeof(int) * length);
if (list == NULL)
{
return (0);
}
current = *head;
while (current != NULL)
{
list[i] = current->n;
current = current->next;
i++;
}
for (j = 0; j < length / 2; j++)
{
if (list[j] != list[length - j - 1])
{
free(list);
return (0);
}
}
free(list);
return (1);
}

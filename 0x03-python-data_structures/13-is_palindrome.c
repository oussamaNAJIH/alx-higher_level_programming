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
if (head == NULL || *head == NULL)
{
return (1);
}
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *previous = NULL;
listint_t *link;
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
link = slow->next;
slow->next = previous;
previous = slow;
slow = link;
}
if (fast != NULL)
{
link = link->next;
}
while (slow != NULL && link != NULL)
{
if (slow->n != link->n)
{
return (0);
}
slow = slow->next;
link = link->next;
}
return (1);
}

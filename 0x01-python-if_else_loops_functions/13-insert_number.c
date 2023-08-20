#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in the new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
        	return (NULL);

	new->n = number;
	new->next = NULL;
	current = *head;
	prev = NULL;
	
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	if (prev == NULL)
	{
        	new->next = *head;
	        *head = new;
	}
	else
   	{
	        new->next = prev->next;
        	prev->next = new;
    	}

	return (new);
}

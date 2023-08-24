#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * rev_listint - reverses a listint_t linked list
 * @head: pointer to pointer of the first node of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *rev_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *f_half, *s_half;
	listint_t *slow = *head, *fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	s_half = rev_listint(&slow);
	f_half = *head;

	while (f_half != NULL && s_half != NULL)
	{
		if (f_half->n != s_half->n)
			return (0);
		f_half = f_half->next;
		s_half = s_half->next;
	}
	return (1);
}

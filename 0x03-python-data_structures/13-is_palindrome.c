#include "lists.h"

/**
 * is_palindrome - a function that check palindrome.
 * @head: list head.
 * Return: 0 (not a palindrome), 1 (palindrome).
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (auxx_palind(head, *head));
}

/**
 * auxx_palind - a function that checks palindrome.
 * @head: list head.
 * @end: list end.
 * Return: nothing.
 */

int auxx_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (auxx_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

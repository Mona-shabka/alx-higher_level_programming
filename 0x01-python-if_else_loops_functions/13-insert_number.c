#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - a function that inserts node in list.
 * @head: head pointer.
 * @number: number should be iserted.
 * Return: number inserted to node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n_node = *head, *n_new = malloc(sizeof(listint_t));

	if (!n_new)
		return (NULL);

	n_new->n = number;
	n_new->next = NULL;

	if (!n_node || n_new->n < n_node->n)
	{
		n_new->next = n_node;
		return (*head = n_new);
	}
	while (n_node)
	{
		if (!n_node->next || n_new->n < n_node->next->n)
		{
			n_new->next = n_node->next;
			n_node->next = n_new;
			return (n_node);
		}
		n_node = n_node->next;
	}
	return (NULL);
}

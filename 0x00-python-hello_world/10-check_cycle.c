#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - a function that checks cycle.
 * @list: list pointer.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *s = list, *f = list;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (f == s)
			return (1);
	}
	return (0);
}

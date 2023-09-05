#include "lists.h"
/**
 * insert_node - function that insert a node without losing sorting list
 * @head: pointer to head of the list
 * @number: data of the node
 * Return: the node to be added if Success or NULL if Failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *previous;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	current = *head;
	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}
	new->next = current;
	previous->next = new;
	return (new);
}
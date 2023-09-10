#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if list is a palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    static listint_t *temp;

    if (current == NULL)
        return (1);
    if (temp == NULL)
        temp = current;
    if (is_palindrome(&current->next) && temp->n == current->n)
    {
        temp = temp->next;
        current = current->next;
        return (1);
    }
    temp = current;
    return (0);
}
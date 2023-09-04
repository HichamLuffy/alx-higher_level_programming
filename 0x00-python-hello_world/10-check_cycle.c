#include "lists.h"
/**
 * check_cycle - check the code
 * @list: parameter
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
    listint_t *pt1 = list;
    listint_t *pt2 = list;

    while (pt1 && pt2 && pt2->next)
    {
        pt1 = pt1->next;
        pt2 = pt2->next->next;

        if (pt1 == pt2)
            return (1);
    }
    return (0);
}
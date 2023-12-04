#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev, *temp, *mid;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    slow = fast = *head;
    mid = NULL;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        mid = slow;
        slow = slow->next;
    }

    prev->next = NULL;

    while (slow != NULL)
    {
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    slow = prev;
    fast = *head;

    while (slow != NULL)
    {
        if (slow->n != fast->n)
            return (0);

        slow = slow->next;
        fast = fast->next;
    }

    return (1);
}

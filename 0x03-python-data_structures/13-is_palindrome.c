#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - The function that reverses a linked list.
 * @head: The pointer to the head of the list.
 *
 * Return: The pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *next = NULL;

	while (head != NULL)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return (prev);
}

/**
 * find_middle - The function finds the middle of the list.
 * @head: The pointer to the head of the list.
 * @prev_of_slow: The pointer to store the previous node of slow pointer.
 *
 * Return: The pointer to the middle node.
 */
listint_t *find_middle(listint_t *head, listint_t **prev_of_slow)
{
	listint_t *slow = head, *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		*prev_of_slow = slow;
		slow = slow->next;
	}
	return (slow);
}

/**
 * compare_halves - The function compares the first and second half of the
 * list.
 * @head: The pointer to the head of the first half.
 * @second_half: The pointer to the head of the reversed second half.
 *
 * Return: 1 if both halves are identical, 0 otherwise.
 */
int compare_halves(listint_t *head, listint_t *second_half)
{
	while (head != NULL && second_half != NULL)
	{
		if (head->n != second_half->n)
		{
			return (0);
		}
		head = head->next;
		second_half = second_half->next;
	}
	return (1);
}

/**
 * is_palindrome - The function that checks if a singly linked list is a
 * palindrome.
 * @head: The double pointer to the head of the list.
 *
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *second_half, *prev_of_slow = NULL;
	listint_t *second_half_copy;
	int is_palindrome;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	slow = find_middle(*head, &prev_of_slow);

	/* Handle odd number of elements */
	if (slow->next != NULL)
	{
		slow = slow->next;
	}

	/* Reverse the second half of the list */
	second_half = reverse_list(slow);
	second_half_copy = second_half;

	/* Compare the first and the reversed second half */
	is_palindrome = compare_halves(*head, second_half);

	/* Restore the original list */
	reverse_list(second_half_copy);
	if (prev_of_slow != NULL)
	{
		prev_of_slow->next = second_half_copy;
	}

	return (is_palindrome);
}

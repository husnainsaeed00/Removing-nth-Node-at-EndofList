# Removing-nth-Node-at-EndofList
Remove Nth Node From End of Linked List
This program solves the problem of removing the nth node from the end of a linked list. Given the head of a linked list and an integer n, the program removes the nth node from the end and returns the modified linked list.

Example
Input:


head = 1 -> 2 -> 3 -> 4 -> 5
n = 2
Output:


Modified Linked List: 1 -> 2 -> 3 -> 5
Implementation Details
The program implements the removal of the nth node from the end of the linked list using a two-pass algorithm. Here's how the program works:

Define a ListNode class to represent each node of the linked list, including the val and next attributes.
Create a Solution class that contains the removeNthFromEnd method.
Inside the removeNthFromEnd method:
Create a dummy node as the head of the list to handle edge cases.
Calculate the length of the linked list by traversing it once.
Find the position of the node to remove from the end by subtracting n from the length.
Traverse to the node before the one to be removed.
Remove the nth node by updating the next pointer of the previous node to skip the node to be removed.
Return the head of the modified linked list.
Usage
To run the program and remove the nth node from the end of a linked list, follow these steps:

Ensure you have Python installed on your system.
Create a new Python file or open an existing one.
Copy the ListNode and Solution class definitions into your file.
Create an instance of the Solution class.
Define the linked list by creating ListNode objects and connecting them using the next attribute.
Call the removeNthFromEnd method on the Solution instance, passing the head of the linked list and the value of n.
Capture the modified linked list returned by the method.
Print or display the modified linked list as desired.
Feel free to modify the code or integrate it into your own codebase as needed. Enjoy removing the nth node from the end of linked lists!

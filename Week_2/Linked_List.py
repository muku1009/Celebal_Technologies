# Step 1: Define the Node class
class Node:
    def __init__(self, data):
        self.data = data        # Store the data
        self.next = None        # Pointer to the next node


# Step 2: Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None        # Initially, the list is empty

    # Step 3: Add nodes to the end of the list
    def add_node(self, data):
        new_node = Node(data)

        # If the list is empty, new node becomes the head
        if not self.head:
            self.head = new_node
            return

        # Traverse to the last node and append the new node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Step 4: Print the linked list
    def print_list(self):
        if not self.head:
            print("Linked List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Step 5: Delete the nth node (1-based index)
    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.\n")

        if n <= 0:
            raise IndexError("Index must be a positive integer.\n")

        # Deleting the head node
        if n == 1:
            print(f"Deleting node at position {n} with value {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 1

        # Traverse to the nth node
        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of range.")

        print(f"Deleting node at position {n} with value {current.data}")
        prev.next = current.next


# Step 6: Test the linked list implementation
if __name__ == "__main__":
    # Create a LinkedList instance
    ll = LinkedList()

    # Add sample nodes to the list
    for value in [10, 20, 30, 40, 50]:
        ll.add_node(value)

    print("\nOriginal Linked List:")
    ll.print_list()
    print("\n")

    # Delete 3rd node (value = 30)
    try:
        ll.delete_nth_node(3)
        print("\nLinked List after deleting 3rd node:")
        ll.print_list()
    except Exception as e:
        print(f"Error: {e}")

    # Try deleting an out-of-range node
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print(f"\nError: {e}")

    # Try deleting from an empty list
    empty_ll = LinkedList()
    try:
        empty_ll.delete_nth_node(1)
    except Exception as e:
        print(f"\nError: {e}")

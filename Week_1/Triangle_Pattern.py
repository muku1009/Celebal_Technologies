# Lower Traingular Pattern
def lower_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)


# Upper Traingular Pattern
def upper_triangle(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)


# Pyramid Pattern
def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))



# Example usage
n = 5
print("Lower Triangle:")
lower_triangle(n)

print("\nUpper Triangle:")
upper_triangle(n)

print("\nPyramid:")
pyramid(n)

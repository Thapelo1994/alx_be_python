def draw_square(n):
  """Draws a solid square pattern of size n with asterisks."""
  for i in range(n):
    for j in range(n):
      print('*', end='')
    print()

# Example usage for a size of 4
draw_square(4)
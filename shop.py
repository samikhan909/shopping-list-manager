shopping_list = ["cheery","banana","watermelon","apple"]  

def put(item):
  """Adds an item ("mango") to the end of the list S."""
  shopping_list.append(item)

def remove(item):
  """Removes the first occurrence of the specified item from the list Shopping.
  Raises a ValueError if the item is not found."""
  try:
    shopping_list.remove(item)
  except ValueError:
    print("Item not found in the list.")

def show():
  """Prints the contents of the list Shopping."""
  if shopping_list:
    print(shopping_list)
  else:
    print("The list is empty.")

def end():
  """Exits the program."""
  exit()

while True:
  print("Menu:")
  print("1. Put (add an item)")
  print("2. Remove (delete an item)")
  print("3. Show (list contents)")
  print("4. End")

  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    item = input("Enter the item to add: ")
    put(item)
    print(f"Item '{item}' added successfully.")
  elif choice == '2':
    item = input("Enter the item to remove: ")
    remove(item)
  elif choice == '3':
    show()
  elif choice == '4':
    end()
  else:
    print("Invalid choice. Please enter a number between 1 and 4.")

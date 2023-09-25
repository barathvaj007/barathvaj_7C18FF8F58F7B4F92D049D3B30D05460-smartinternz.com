class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance):
    self._account_number = account_number
    self._account_holder_name = account_holder_name
    self._account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self._account_balance += amount
      print(
          f"Deposited ₹{amount:.2f}. New balance: ₹{self._account_balance:.2f}"
      )
    else:
      print("Invalid deposit amount.")

  def withdraw(self, amount):
    if 0 < amount <= self._account_balance:
      self._account_balance -= amount
      print(
          f"Withdrew ₹{amount:.2f}. New balance: ₹{self._account_balance:.2f}")
    else:
      print("Invalid withdrawal amount or insufficient funds.")

  def display_balance(self):
    print(
        f"Account Balance for {self._account_holder_name}: ₹{self._account_balance:.2f}"
    )


# Test the BankAccount class
account_number = input("Enter account number: ")
account_holder_name = input("Enter account holder name: ")

try:
  initial_balance = float(input("Enter initial balance: "))
except ValueError:
  print("Invalid initial balance. Please enter a valid number.")
  exit(1)

account = BankAccount(account_number, account_holder_name, initial_balance)

while True:
  print("\nMenu:")
  print("1. Deposit")
  print("2. Withdraw")
  print("3. Display Balance")
  print("4. Exit")
  try:
    choice = int(input("Enter your choice: "))
  except ValueError:
    print("Invalid choice. Please select a valid option.")
    continue

  if choice == 1:
    try:
      amount = float(input("Enter the deposit amount: "))
    except ValueError:
      print("Invalid deposit amount. Please enter a valid number.")
      continue
    account.deposit(amount)
  elif choice == 2:
    try:
      amount = float(input("Enter the withdrawal amount: "))
    except ValueError:
      print("Invalid withdrawal amount. Please enter a valid number.")
      continue
    account.withdraw(amount)
  elif choice == 3:
    account.display_balance()
  elif choice == 4:
    print("Thank you for using the BankAccount program. Goodbye!")
    break
  else:
    print("Invalid choice. Please select a valid option.")

original_pin = "1234"
entered_pin = input("enter your pin:")

while entered_pin != original_pin:
    print("pin is incorrect, retry!")
    entered_pin = input("enter your pin: ")
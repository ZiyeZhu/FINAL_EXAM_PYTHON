# Task 4: Collect numbers from user until "done", then print total, count, and average
print("\nTask 4: Number Collector")
number_list = []
while True: #loop until the user enters "done"
    user_input = input("Enter a number (or 'done' to finish): ").strip() #ask the user to enter a number or "done" to finish
    if user_input.lower() == "done": #if the user enters "done", break out of the loop
        break
    if user_input == "":
        print("Invalid input. Try again.") #if the user enters nothing, ask for input again
        continue
    try:
        num = float(user_input)
        number_list.append(num)
    except ValueError:
        print("Invalid input. Try again.") #if the user enters a non-numeric value, ask for input again


if number_list:
    total = sum(number_list)
    count = len(number_list)
    average = round(total / count, 2)
    print(f"Total entries: {count}")
    print(f"Total sum: {total}")
    print(f"Average: {average}")
else:
    print("No valid numbers entered.")
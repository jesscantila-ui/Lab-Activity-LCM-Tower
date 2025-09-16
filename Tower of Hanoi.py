try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in user_input.split()]

    print(f"\nInput values = {numbers}")

    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            print(f"Items compared: [{numbers[j]}, {numbers[j+1]}]", end=" ")
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                print("swapped")
            else:
                print("not swapped")

    print(f"Output values = {numbers}")

except ValueError:
    print("Invalid input! Please enter integers only.")
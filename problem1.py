def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def gcd(a, b): #this will be used to calculate the lcm, so it is needed too.
    if b == 0:
        return a
    return gcd(b, a % b)

try:
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))

    if x <= 0 or y <= 0:
        print("Error: Please enter positive integers only.")
    else:
        print(f"The LCM of {x} and {y} is = {lcm(x, y)}")

except ValueError:
    print("Please enter integers only.")

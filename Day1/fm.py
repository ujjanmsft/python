num = int(input("Enter a number: "))
print("\nMulplication table for {num}:")
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
    
number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    product = i * number
    print(f"{number} x {i} = {product}", end="\t")
print()



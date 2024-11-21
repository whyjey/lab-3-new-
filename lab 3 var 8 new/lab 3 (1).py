# Зчитування двох чисел
num1 = int(input("Введіть перше тризначне число: "))
num2 = int(input("Введіть друге тризначне число: "))

# Обчислення останніх цифр
last_digit1 = num1 % 10
last_digit2 = num2 % 10

# Сума і добуток останніх цифр
sum_of_digits = last_digit1 + last_digit2
product_of_digits = last_digit1 * last_digit2

# Виведення результатів
print(f"Сума останніх цифр: {sum_of_digits}")
print(f"Добуток останніх цифр: {product_of_digits}")

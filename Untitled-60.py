
quantity = int(input("Введіть кількість товару: "))
price = float(input("Введіть ціну одного товару: "))
discount = float(input("Введіть знижку у відсотках: "))

if quantity > 0 and price > 0 and 0 <= discount <= 50:
    total = quantity * price
    discount_sum = total * discount / 100
    result = total - discount_sum

    print("Початкова вартість:", total)
    print("Сума знижки:", discount_sum)
    print("До сплати:", result)

    if result <= 5000:
        print("Покупка відповідає встановленому ліміту.")
    else:
        print("Покупка перевищує ліміт 5000 грн.")
else:
    print("Помилка! Перевірте введені дані.")

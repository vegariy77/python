price_product = int(input("Сколько стоит товар? "))
discount = int(input("Сколько стоставляет процент скидки? "))
procent_discount = (price_product * discount) / 100
print(f"Цена со скидкой: {price_product - procent_discount}")
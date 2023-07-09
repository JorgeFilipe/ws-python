# 1 identifier chip = 4 R$
# 2 food identifier ring = 3.50 R$

chicken_amount=int(input("Enter the amount of chickens in your farm: "))

id_chip=4
food_id_ring=3.50

totalSpent=(((chicken_amount*2)*food_id_ring)+(chicken_amount*id_chip))

print(f"Total spent to mark all chickens is: R$ {totalSpent}")
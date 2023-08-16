rate = int(input("Crit Rate: "))
damage = int(input("Crit Damage: "))
maxRate = rate + damage / 2
maxDamage = rate * 2 + damage
print(f"Max Crit Rate: {maxRate}\nMax Crit Damage: {maxDamage}")
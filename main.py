from random import *

defaultAtk = 1000
totalDamage = 0

rate = int(input("Crit Rate: "))
damage = int(input("Crit Damage: "))

maxRate = rate + damage / 2
maxDamage = rate * 2 + damage
print(f"Max Crit Rate: {maxRate}\nMax Crit Damage: {maxDamage}")

for i in range(10):
    if randint(0,100) <= rate:
        totalDamage += 1000 + 1000 * damage * 0.01
    else: 
        totalDamage += 1000

print(totalDamage / 100)
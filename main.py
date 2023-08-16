from random import *

defaultAtk = 1000
totalDamage = 0

rate = int(input("Crit Rate: "))
damage = int(input("Crit Damage: "))

maxRate = rate + damage / 2
maxDamage = rate * 2 + damage
print(f"Max Crit Rate: {maxRate}\nMax Crit Damage: {maxDamage}")

print(f"1000 ATK Default Crit DMG: {1000 + defaultAtk * rate * 0.01 * damage * 0.01}")
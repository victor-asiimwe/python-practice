bibleschool = "https://bibleschool.com"
print(bibleschool.removeprefix('https://'))

bibleschool = "https://bibleschool.com"
final = f"{bibleschool.removeprefix('https://')}"
print(final)

read = "www.readthebible_daily"
print(read.removeprefix('www.'))

Just_1 = "Sir. Jim"
Just_2 = f"{Just_1.removeprefix('Sir.')}"
Just_3 = f"{Just_2.lstrip()}"
print(Just_3)

Just_1 = "Sir. Jim"
Just_2 = f"{Just_1.removeprefix('Sir.').lstrip()}"
print(Just_2)

Just_1 = "Sir. jim"
Just_2 = f"{Just_1.removeprefix('Sir.').lstrip().title()}"
print(Just_2)
#In this code I removed both the prefix and suffix and I stripped off space on the left of the value and also converted info to title case
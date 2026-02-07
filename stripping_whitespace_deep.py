Heaven_1 = "God is Lord   "
Heaven_1 = Heaven_1.rstrip()
Heaven_2 = "  john the baptist"
Heaven_2 = Heaven_2.lstrip()
Heaven_3 = "   god is lord   "
Heaven_3 = Heaven_3.strip()
Heavens = f"{Heaven_1.upper()} \n{Heaven_2.title()} \n{Heaven_3.title()}"
print(Heavens)
#In this program I stripped space on the right of the value in line 1 and on the left in line 3 and on both sides in line 7 while also converting them title case
Heaven = "Jesus is Lord   "
Heaven = Heaven.rstrip()
print(Heaven)

Heaven = "  Jesus is Lord"
Heaven = Heaven.lstrip()
print(Heaven)

Heaven = "   Jesus is Lord   "
Heaven = Heaven.strip()
print(Heaven)

Heaven_1 = "Jesus is Lord   "
Heaven_1 = Heaven_1.rstrip()
Heaven_2 = "  jesus is lord"
Heaven_2 = Heaven_2.lstrip()
Heaven_3 = "   jesus is lord   "
Heaven_3 = Heaven_3.strip()
Heavens = f"{Heaven_1.upper()} \n{Heaven_2.title()} \n{Heaven_3.lower()}"
print(Heavens)
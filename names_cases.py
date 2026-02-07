Jesus = "I love you"
Final = f"Hello, {Jesus.title()}!"
print(Final)

Name_1 = "siima daisy pamela"
Name_2 = "siima daisy pamela"
Name_3 = "siima daisy pamela"
final = f"{Name_1.title()} \n{Name_2.upper()} \n{Name_3.lower()}"
print(final)

quote = '"A person who never made a mistake never tried anything new."'
final = f"Albert Einstein once said, {quote}"
print(final)

name = "Jesus "
print(name.rstrip())

name = " Jesus"
print(name.lstrip())

name = " Jesus "
print(name.strip())

name_1 = "Jesus "
name_2 = " Jesus"
name_3 = " Jesus "
final = f"{name_1.rstrip()} \n\t{name_2.lstrip()} \n\t{name_3.strip()}"
print(final)

filename = "jobwasgoodtoGod.pdf"
final = f"{filename.removesuffix('.pdf')}"
print(final)

filename = "www.jobwasgoodtoGod"
final = f"{filename.removeprefix('www.')}"
print(final)

filename = "www.jobwasgoodtoGod.pdf"
final = f"{filename.removeprefix('www.').removesuffix('.pdf')}"
print(final)
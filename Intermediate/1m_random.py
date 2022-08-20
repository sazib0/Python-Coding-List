import random
bars = ["Shoolbred's","The Wren","The Scratcher","ACME","Blind Barber"]

people = ["Mattan","Chris","that person you forgot to text back","Kanye West","Samuel L. Jackson"]

random_bar = random.choice(bars)
random_person = random.choice(people)

print(f"How about you go to {random_bar} with {random_person}?")
#The f is for formatting. When you use this in your code, you are able to substitute variables into the string. 
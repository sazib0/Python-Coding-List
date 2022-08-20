import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]
male = ["Mattan",
        "Chris",
        "that guy you forgot to text back",
        "Kanye West",
        "Samuel L. Jackson",
         "Peter"]
female = ["Jeanette",
          "Adele",
          "that girl you saw on the bus",
          "Britney",
          "Meryl Streep",
          "Sandra"]
random_bar = random.choice(bars)
random_male = random.choice(male)
random_female = random.choice(female)
print(f"How about you go to {random_bar} with {random_male} and {random_female}")
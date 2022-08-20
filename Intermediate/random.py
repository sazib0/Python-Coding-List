# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 23:24:07 2021

@author: sazib
"""

import random

bars = ["Shoolbred's",

        "The Wren",

        "The Scratcher",

        "ACME",

        "Blind Barber"]

people = ["Mattan",

          "Chris",

          "that person you forgot to text back",

          "Kanye West",

          "Samuel L. Jackson",

          "Your ex",

          "Charles"]

random_bar = random.choice(bars)

random_person = random.choice(people)

random_person_1 = random.choice(people)

print(f"How about you go to {random_bar} with {random_person}, {random_person_1}")
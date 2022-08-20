# You just completed your first coding challenge! Cheers to you! In this lesson, I'll walk you through the solution to the challenge. I'll show you how to add data to a Python List, change the output of printed information and points out some syntax errors that you can run into—giving you a brief introduction to debugging, which will be covered in more depth in later lessons.

# 1. Change Samule L. Jackson's name 
# This one's pretty straightforward. All you have to do is go in and correct Colonel Nick Fury's name to Samuel L. Jackson, and remember to save the Sublime file before you try running the script in your terminal. 

# 2. Add another person to the 'people' list
# Simply type another name, and add a comma, so it would look like this: 

# people = ["Mattan",
#           "Chris",
#           "that person you forgot to text back",
#           "Kanye West",
#           "Samuel L. Jackson",
#           "Kosta"]
# Again, remember to consistently save your work.  

# 3. Add another person 
# This one is more involved. First, you have to create another category, like this: 

# random_bar = random.choice(bars)
# random_person_one = random.choice(people)
# random_person_two = random.choice(people)
# And then you go to your function, and add it in. 

# print(f"How about you go to {random_bar} with {random_person_one} and {random_person_two}?")
# Remember to save, and you're all set to run the script! 

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

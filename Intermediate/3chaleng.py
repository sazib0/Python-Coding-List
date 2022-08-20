file = "amazon_most_wished_books100_122019.xlsx"

df = pd.read_excel(file, sheet_name=0)

books = df['Book'].tolist()

friend_name=input("Please enter the name of your friend: ")

print(f"What book you can gift to {friend_name}?")

random_books = random.choice(books)

print(f"You can gift to {friend_name} the book {random_books}") #We can also add to this result the link to buy
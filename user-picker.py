import random

# Open the CSV file and read the content
with open('cleaned_file_2.csv', 'r') as file:
    content = file.read()

# Split the content by commas to get the usernames
usernames = content.strip().split(',')

# Pick a random username
winner = random.choice(usernames)

# Print the randomly selected username (winner)
print(f"Simracingkulubu 10 Ekim Çekilişinin kazananı: {winner}")

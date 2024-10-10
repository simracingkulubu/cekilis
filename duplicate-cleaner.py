# Open the CSV file and read the content
with open('fixed_file_2.csv', 'r') as file:
    content = file.read()

# Split the content by commas and remove any extra spaces/newlines
usernames = content.strip().split(',')

# Remove duplicates while preserving the original order
unique_usernames = []
for username in usernames:
    if username not in unique_usernames:
        unique_usernames.append(username)

# Join the unique usernames back into CSV format
cleaned_csv = ','.join(unique_usernames)

# Write the cleaned CSV to a new file
with open('cleaned_file_2.csv', 'w') as file:
    file.write(cleaned_csv)

print("Duplicates removed and saved to 'cleaned_file_2.csv'")

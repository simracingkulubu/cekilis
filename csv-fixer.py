# Open the input file and read lines
with open('raw.csv', 'r') as file:
    lines = file.readlines()

# Remove any extra newlines or spaces, and join them with commas
csv_content = ','.join([line.strip() for line in lines])

# Write the fixed CSV structure to a new file
with open('fixed_file_2.csv', 'w') as file:
    file.write(csv_content)

print("Fixed CSV structure saved to 'fixed_file.csv'")

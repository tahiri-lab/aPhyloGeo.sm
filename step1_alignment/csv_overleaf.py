# Open the CSV file for reading
with open('data_refTable1.csv', 'r') as file:
    csv_content = file.read()
# print(csv_content)
# Replace commas with ampersands
csv_content_modified = csv_content.replace(',', '&')

# Open the same CSV file for writing and overwrite its contents
with open('overleaf_refTable1.csv', 'w') as file:
    file.write(csv_content_modified)

print("Commas replaced with ampersands.")

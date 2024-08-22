import pandas as pd

# Load the CSV file
csv_file = 'data.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file, encoding='ISO-8859-1')  # Use the correct encoding

# Print the DataFrame to verify data extraction
print(df.head())

# Group data into sections
pages = []
for i in range(0, len(df), 3):
    sections = []
    for j in range(3):
        if i + j < len(df):
            row = df.iloc[i + j]
            sections.append({
                'header': row['Header'],      # Adjust these column names as per your CSV
                'textbox1': row['Textbox1'],
                'textbox2': row['Textbox2']
            })
    pages.append(sections)

# Print the grouped data
for page_num, sections in enumerate(pages):
    print(f"Page {page_num + 1}: {sections}")

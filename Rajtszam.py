import pandas as pd
from jinja2 import Environment, FileSystemLoader
import os

# Load the data from CSV
df = pd.read_csv('data.csv')

# Setup Jinja2 environment
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)
template = env.get_template('template.html')

# Prepare the data for the template
sections = []
for _, row in df.iterrows():
    sections.append({
        'header': row['Header'],
        'textbox1': row['Textbox1'],
        'textbox2': row['Textbox2'],
        'background_color': 'rgb(255,192,0)',  # Placeholder, will be overridden by JS
        'drink': row['Drink'],
        'shape': row['Shape']
    })

# Render the HTML
html_output = template.render(sections=sections)

# Write the output to a file with UTF-8 encoding
os.makedirs('Print', exist_ok=True)
with open('Print/output.html', 'w', encoding='utf-8') as file:
    file.write(html_output)

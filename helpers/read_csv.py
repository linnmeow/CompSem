import pandas as pd

# Specify the path to your CSV file
csv_file_path = 'final_de.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Extract the values from the "sentence" column and put them in a list
sentence_list = df['sentence'].tolist()

# Display the list of sentences
print(sentence_list)

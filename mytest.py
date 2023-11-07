# Path to the provided JSONL file
file_path = 'data/BillSum/billsum_test_with_oracle.jsonl'
output_path = 'billsum_test_with_oracle.jsonl'

# Number of elements to keep
num_elements_to_keep = 5

# Initialize an empty list to store the first 50 elements
trimmed_data = []

# Open the original file and read the first 50 elements
with open(file_path, 'r') as file:
    for i, line in enumerate(file):
        if i < num_elements_to_keep:
            trimmed_data.append(line.strip())
        else:
            break

# Write the first 50 elements to a new JSONL file
with open(output_path, 'w') as file:
    for item in trimmed_data:
        file.write(item + '\n')
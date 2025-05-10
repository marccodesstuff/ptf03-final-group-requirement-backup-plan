import csv

def get_unique_column_data(file_path, column_name):
    unique_data = set()
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if column_name in row:
                    unique_data.add(row[column_name])
                else:
                    raise ValueError(f"Column '{column_name}' not found in the CSV file.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return unique_data

def save_unique_values_to_file(unique_values, output_file):
    try:
        with open(output_file, mode='w', encoding='utf-8') as file:
            for value in unique_values:
                file.write(f"{value}\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Example usage
if __name__ == "__main__":
    file_path = "International_Education_Costs.csv"  # Replace with your CSV file path
    column_name = "Country"  # Replace with the column name you want to extract
    output_file = "unique_values.txt"  # Output file to save unique values

    unique_values = get_unique_column_data(file_path, column_name)
    save_unique_values_to_file(unique_values, output_file)
    print(f"Unique values in column '{column_name}' have been saved to '{output_file}'.")
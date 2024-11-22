import pandas as pd

def split_csv_large(file_path, output_file1, output_file2, chunk_size=100000):
    """
    Splits a large CSV file into two approximately equal parts.
    Processes the file in chunks to avoid memory issues.
    """
    # Open output files
    with open(output_file1, 'w') as f1, open(output_file2, 'w') as f2:
        reader = pd.read_csv(file_path, chunksize=chunk_size, iterator=True)
        
        # Write header to both files
        header_written = False
        row_count = 0
        
        for chunk in reader:
            if not header_written:
                # Write header once to both files
                chunk.to_csv(f1, index=False)
                chunk.to_csv(f2, index=False, header=False)
                header_written = True
            else:
                # Write data rows to the appropriate file
                if row_count < chunk_size // 2:
                    chunk.to_csv(f1, index=False, header=False)
                else:
                    chunk.to_csv(f2, index=False, header=False)
            
            # Increment the row counter
            row_count += len(chunk)
            
        print(f"CSV split into '{output_file1}' and '{output_file2}'.")

file_path = "set2/synthetic_fraud_data.csv"  # Replace with your CSV file path
output_file1 = "set2/split_part1_synthetic_fraud_data.csv"
output_file2 = "set2/split_part2_synthetic_fraud_data.csv"

split_csv_large(file_path, output_file1, output_file2)
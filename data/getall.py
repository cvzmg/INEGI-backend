import pandas as pd
import os

if __name__ == "__main__":
    # List of file paths to read
    file_paths = [
        "./output/work.csv",
        "./output/sport_centers.csv",
        "./output/schools.csv",
        "./output/religion.csv",
        "./output/married.csv",
        "./output/cultural.csv",
        "./output/budget.csv",
        "./output/ages.csv",
        "./output/housing_state.csv",
        "./output/recreational.csv",
        "./output/security_for_women.csv",
        "./output/security_everyone.csv",
        "./output/green_spaces.csv",
        "./output/health_centers.csv",
        "./output/restaurant.csv",
        "./output/transportation.csv",
    ]

    # Output text file
    output_file = "combined_data.txt"

    # Open the output file in write mode
    with open(output_file, 'w') as outfile:
        # Iterate through each file path
        for file_path in file_paths:
            try:
                # Add a header to indicate the start of a new file's content
                outfile.write(f"--- Content from: {os.path.basename(file_path)} ---\n\n")
                
                # Open and read the content of the current CSV file
                with open(file_path, 'r') as infile:
                    content = infile.read()
                    outfile.write(content)
                
                # Add newlines for separation between files
                outfile.write("\n\n")
            except FileNotFoundError:
                outfile.write(f"--- File not found: {file_path} ---\n\n")

    print(f"All data has been written to {output_file}")

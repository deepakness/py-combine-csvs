import os
import glob
import pandas as pd

# Set working directory to folder containing CSV files
os.chdir("CSVs")

# Get list of all CSV files in folder
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# Combine all CSV files into one DataFrame
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

# Create directory 'Combined CSV' if it doesn't exist
if not os.path.exists('Combined'):
    os.makedirs('Combined')

# Write combined DataFrame to CSV file in directory 'Combined CSV'
combined_csv.to_csv("Combined/combined_csv.csv", index=False, encoding='utf-8-sig')

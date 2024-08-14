import os
import sys
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi
import datetime

# Step 1: Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Step 2: Define dataset and file path
dataset = "piterfm/paris-2024-olympic-summer-games"  # Replace with the actual dataset name
download_path = 'path_for_the_file'
# Step 3: Remove existing files if they exist
if os.path.exists(download_path):
    for root, dirs, files in os.walk(download_path):
        for file in files:
            os.remove(os.path.join(root, file))
    print(f"Existing files in {download_path} have been removed.")

# Step 4: Download dataset and unzip
api.dataset_download_files(dataset, path=download_path, unzip=True)

# Step 5: Unzip the file if it was downloaded as a zip
zip_file = os.path.join(download_path, f"{dataset.split('/')[-1]}.zip")
if os.path.exists(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(download_path)
    os.remove(zip_file)  # Remove the zip file after extraction

print(f"{dataset} has been downloaded and unzipped.")

file = open(r'path_where_you_want_to_log','a')

file.write(f'{datetime.datetime.now()} - The Script ran successfully. \n')

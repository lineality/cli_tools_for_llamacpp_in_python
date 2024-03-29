"""
For use with Jan or another directory of models,
this will return a list of optional gguf model-paths
for the llama-cpp api
"""

import os

def find_folders_and_files_with_gguf(base_path):
    folders_and_files_with_gguf = []
    # Iterate through all items in base path
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Check each file in the directory
            for file in os.listdir(item_path):
                # Check if the file ends with '.gguf'
                if file.endswith('.gguf'):
                    # Construct the desired string format: basefolder/filename
                    result = f"{item}/{file}"
                    folders_and_files_with_gguf.append(result)
                    break  # Found a matching file, no need to check the rest
    return folders_and_files_with_gguf

# Base path where to search for folders and gguf files
base_path = '/home/oops/jan/models'

# Call the function and print the result
folders_and_files = find_folders_and_files_with_gguf(base_path)
for result in folders_and_files:
    print(f"Model @->  {result}")

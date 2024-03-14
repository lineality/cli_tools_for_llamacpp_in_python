# cli_tools_for_llamacpp_in_python

Preliminary tools for using llama.cpp e.g. selecting a model and using
a local gguf model instead of a paid cloud api.

#### Notes:
- system prompts and conversation history 'context' are still not clear, not well implimented yet. 


- save history as...file?
- read in file as instruct?
(separate files to avoid formatting issues?
- 
sample:
translate 'sign up' into french, with your translation between pipes |translation| and other commentary outside

# To use:
1. close repo and cd inside (cd -> change directory)
2. set path_to_model_foler as it exists on your system
3. Run:
```python
python call_llamacapp.py
```


# TODO
- maybe make an instruct...doc maker reader...thing
- 


try using list to csv:

```python
import csv

# Function to write data to a CSV file
def write_values_to_csv(file_path, data, header=None):
    """
    Writes given data to a CSV file.
    
    :param file_path: str, the path to the CSV file to be written.
    :param data: list of lists, where each inner list represents a row in the CSV.
    :param header: list, optional header row. If provided, it will be written as the first row in the file.
    """
    # Open the file in write mode ('w') with newline='' to prevent adding extra newline characters on Windows
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header first if it's provided
        if header:
            writer.writerow(header)
        
        # Write the data rows
        writer.writerows(data)

# Example usage
if __name__ == "__main__":
    file_path = 'example.csv'
    header = ['Column1', 'Column2', 'Column3']
    data = [
        [1, 'Apple', 2.5],
        [2, 'Banana', 3.5],
        [3, 'Cherry', 4.5]
    ]
    
    write_values_to_csv(file_path, data, header)
    print(f"Data has been successfully written to {file_path}")
```
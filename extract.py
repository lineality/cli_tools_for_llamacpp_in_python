
def add_ranks_votes_to_candidate(vote_list, candidate_dictionary):
    """
    Adds each item from vote_list to the list in candidate_dictionary corresponding to the item's sequence position,
    where the sequence position is mapped to alphabetical keys ('a', 'b', 'c', etc.).

    :param vote_list: List of numbers to be added.
    :param candidate_dictionary: Dictionary with alphabetical keys representing sequence positions and values as lists.
    """
    # Create a list of keys from the dictionary to map index to keys
    keys = list(candidate_dictionary.keys())

    for index, value in enumerate(vote_list):
        # Ensure the index is within the range of available keys
        if index < len(keys):
            # Append the item to the list for the corresponding key based on sequence position
            candidate_dictionary[keys[index]].append(value)
        else:
            # Optionally handle or log if the index exceeds the available keys
            print(f"No key available for index {index} in candidate_dictionary.")
            raise Exception("Index exceeds the number of keys in candidate_dictionary.")

    return candidate_dictionary

# Initialize the dictionary with options and an empty list for each
dict_of_options = {'your_translation': [], 'Dein_Benutzername': [], 'Your_Account_Name': []}

# List of votes to be added
list_of_votes = [10, 10, 9]

# Add the ranks and votes to the candidate dictionary
dict_result = add_ranks_votes_to_candidate(list_of_votes, dict_of_options)

# Print the resulting dictionary
print(dict_result)



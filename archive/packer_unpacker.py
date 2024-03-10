# three inputs to package, six to unpack

"""
Pack & Unpack exported python dictionary:

Please advise on a python function:

six parameters, last three may be blank

to package a dict, include three dictionaries
1. the dict_package_keys_generator() produces 3 non-colliding keys for
    ```
    {
    :
    }
    ```
    so that the python dictionary can be stored as a raw string
    with no formatting problems

    and restored to being a python dictionary from that string
    given the keys.

2. the packer turns the dictionaries into named string files
    and returns the names

3. the unpacker takes the file names and the keys
and restores the dictionaries

the packer and unpacker are the same function,
- packs when 3 keys are blank
- unpacks when 3 keys are present

(or if need be it could be two separte functions)



notes:
1. the goals in not binary serialization, but saving the data in ~readable string form.
2. tree-search through the dictionary and create a tree map of node and leaf values
using unique non-colliding proxies for {}: with no quotes and no-escape characters
take the contents of the dictionary, first version all string, and record it.

unpack:
restore this content doing the reverse of what was done before.



Task:
The current version below works in some cases but IS COMPLETELY WRONG as it uses json.dumps/load
which is broken by natural language character-string formatting. The whole point is
to export and import the dictionary body WITHOUT json, without escape characters, without
using or changing any '"{:} symbols. 

This insane code below makes unique substitution keys AND NEVER USES THEM...
Fix this horrible broken code.


"""
import json
import os
from datetime import datetime, UTC


def dict_package_keys_generator(dict_list, key_quantity=3):
    """
    Produce a set of 3 unique substitution keys
    that do not collide with any contents
    of the three dictionaries,

    to make a dictionary-string storage
    and recovery format
    to send and restor the python dictionaries

    characters important for syntax have been removed

    This is set to 7, but longer strings may have
    a lower change of colliding

    """

    ascii_list = [
        '!',
        '#',
        '$',
        '%',
        '&',
        '*',
        '+',
        ',',
        '-',
        '.',
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        ':',
        ';',
        '<',
        '=',
        '>',
        '?',
        '@',
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z',
        '^',
        '_',
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
        '|',
        '~']
    import random

    output_list = []

    # Randomly select 7 symbols from the list three times.
    for i in range(key_quantity):
        ok_flag = False

        number_of_symbols = 7

        while not ok_flag:

            random_symbols = random.sample(ascii_list, number_of_symbols)

            # Create a string from the randomly selected symbols.
            random_string = "".join(random_symbols)

            dict_string = str(dict_list)

            counter = 0

            # not already selected, not collide with use-case
            if (random_string not in dict_string) and (random_string not in output_list):

                # OK! no collisions, moving on...
                ok_flag = True

            else:
                # if too many colissions happen, increase the number of symbols
                if counter > 100:
                    number_of_symbols += 3

        # Output the random string.
        output_list.append(random_string)

    return output_list


# def pack_unpack_python_objects(dict_list, key_list=None):
#     """
#     Packs dictionaries into named string files when key_list is None.
#     Unpacks dictionaries from named string files when key_list is provided.

#     Parameters:
#     - dict_list: list of dictionaries to pack or a list of filenames to unpack.
#     - key_list: list of substitution keys for unpacking, or None for packing.

#     Returns:
#     - Names of the files and keys when packing.
#     - Dictionaries when unpacking.
#     """
#     if key_list is None:  # Packing mode
#         keys = dict_package_keys_generator(dict_list)
#         filenames = []
#         for i, d in enumerate(dict_list):
#             if d is not None:
#                 # Convert dictionary to string.
#                 dict_str = json.dumps(d)
#                 for key in keys:
#                     # Replace critical characters with unique keys.
#                     dict_str = dict_str.replace(key, f"__{key}__")

#                 ###############
#                 # Save to file
#                 ###############
#                 # make readable time
#                 # from datetime import datetime, UTC
#                 date_time = datetime.now(UTC)
#                 clean_timestamp = date_time.strftime('%Y%m%d%H%M%S%f')

#                 filename = f"dict_{i}_{clean_timestamp}.txt"
                
#                 with open(filename, "w") as file:
#                     file.write(dict_str)
#                 filenames.append(filename)
#         return filenames, keys
#     else:  # Unpacking mode
#         dicts = []
#         for filename in dict_list:
#             if os.path.exists(filename):
#                 with open(filename, "r") as file:
#                     dict_str = file.read()
#                 for key in key_list:
#                     # Restore critical characters from unique keys.
#                     dict_str = dict_str.replace(f"__{key}__", key)
#                 # Convert string back to dictionary.
#                 d = json.loads(dict_str)
#                 dicts.append(d)
#             else:
#                 dicts.append(None)
#         return dicts

# # Example usage:
# # For packing:
# # filenames, keys = pack_unpack_python_objects([dict1, dict2, dict3])
# # For unpacking:
# # dicts = pack_unpack_python_objects(filenames, keys)


import json
import os
from datetime import datetime, UTC

def pack_unpack_python_objects(dict_list, key_list=None):
    """
    Packs dictionaries into named string files when key_list is None.
    Unpacks dictionaries from named string files when key_list is provided.

    Parameters:
    - dict_list: list of dictionaries to pack or a list of filenames to unpack.
    - key_list: list of substitution keys for unpacking, or None for packing.

    Returns:
    - Names of the files and keys when packing.
    - Dictionaries when unpacking.
    """
    directory_name = "packunpack_py"
    os.makedirs(directory_name, exist_ok=True)  # Ensure the directory exists.

    if key_list is None:  # Packing mode
        keys = dict_package_keys_generator(dict_list)
        filenames = []
        for i, d in enumerate(dict_list):
            if d is not None:
                dict_str = json.dumps(d)
                for key in keys:
                    # TODO: changethis make absolutely no sense, there are NO KEYS to replace? this means nothing[]
                    dict_str = dict_str.replace(key, f"__{key}__")

                # Generate a timestamped filename
                # make readable time
                # from datetime import datetime, UTC
                date_time = datetime.now(UTC)
                clean_timestamp = date_time.strftime('%Y%m%d%H%M%S%f')
                filename = f"dict_{i}_{clean_timestamp}.txt"
                absolute_path = os.path.join(directory_name, filename)

                with open(absolute_path, "w") as file:
                    file.write(dict_str)  # Corrected to write using file object
                filenames.append(filename)
        return filenames, keys
    else:  # Unpacking mode
        dicts = []
        for filename in dict_list:
            absolute_path = os.path.join(directory_name, filename)

            if os.path.exists(absolute_path):
                with open(absolute_path, "r") as file:
                    dict_str = file.read()
                for key in key_list:
                    dict_str = dict_str.replace(f"__{key}__", key)
                d = json.loads(dict_str)
                dicts.append(d)
            else:
                dicts.append(None)
        return dicts


#######################
# Tune Your Paramaters
#######################
parameter_dict = {
    '--temp N': 0.8,  # (default value is 0.8)
    '--top-k': 40,    # (selection among N most probable. default: 40)
    '--top-p': 0.9,   # (probability above threshold P. default: 0.9)
    '--min-p': 0.05,  # (minimum probability threshold. default: 0.05)
    '--seed': -1,     # seed, =1 is random seed
    '--tfs': 1,	      # (tail free sampling with parameter z. default: 1.0) 1.0 = disabled
    '--threads': 8,   # (~ set to number of physical CPU cores)
    '--typical': 1,	  # (locally typical sampling with parameter p typical (also like ~Temperature) (default: 1.0, 1.0 = disabled).
    '--mirostat': 2,  # (default: 0,  0= disabled, 1= Mirostat, 2= Mirostat 2.0)
    '--mirostat-lr': 0.05,  # (Mirostat learning rate, eta.  default: 0.1)
    '--mirostat-ent': 3.0,  # (Mirostat target entropy, tau.  default: 5.0)
    '--ctx-size': 500       # Sets the size of the prompt context
    }


model_configs = {
    'name': 'gguf',  # (default value is 0.8)
    'path': 'gguf',  # (default value is 0.8)
    }


#############################
# Use model select + history
#############################
conversation_history = [
    {"role": "system", "content": "You are a friendly assistant."},
    {"role": "user", "content": "Is cooking easy?"},
    {"role": "assistant", "content": "Yes, it is. What shall we cook?"},
    {"role": "user", "content": "Let's make bread."},
    {"role": "assistant", "content": "Here is a good cornbread recipe..."},
    {"role": "user", "content": "What seafood are we cooking now?"},
]


object_list = [parameter_dict, model_configs, conversation_history]

file_names_list, keys_list = pack_unpack_python_objects(object_list)
print(file_names_list)
print(keys_list)

list_of_objects = pack_unpack_python_objects(file_names_list, keys_list)

for i in list_of_objects:
    print(type(i))
    print(i)

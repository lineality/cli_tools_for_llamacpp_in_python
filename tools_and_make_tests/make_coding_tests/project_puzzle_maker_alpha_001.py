"""
1. There is a project.

2. There are R-number of roles/participants (set at the start)

3. There are A-number of arrays
- a starting_project_array
- a final_project_array
- R-number of arrays, one for each role,
where at the start only the starting_project_array is not empty.

4. Each role/participant will have T-number of tasks

5. Each branch of tasks must result in a change to the final_project_array (no dead branches, no branches that lead to no final result)

6. Each task is an operation carried out on either
  A. a slice of any array
  or
  B. the contents of two indices from any array or arrays.
  The result of which is then added any array. (append, insert a change, add at an index, etc.)

  slice operations include: reverse, sort, etc.

  two-index operations include: sum, subtraction, product, exponents, etc.
  (not division because of divide by zero issues) for numbers,
  and for strings there can be other operations such as concatonization or set operations.

7. A Turn-based schedule:
A schedule is created to sequence the total number (T-number * R-number) of tasks,
consistent with there being no dead branches, no branches of tasks that lead to no final result.

8. The project structure is a modular framework that can accomodate 'any'
starting array, given these inputs:
- set R-number of roles
- set T-number of tasks
- set source and sink for each task
- set turn-based-schedule
As a function, the only input to the function is the starting_project_array,
and the output is always the the same for the same input (a phenomenon for which there is, strangely, no clear term).



9. Once the project structure is made, 'unit-tests' for correct expected outputs
given specific inputs of starting_project_array contents need to be made.

10. puzzle-dictionary:
Both the project_structure and U-number of unit tests (say, five)
are published/reported, such that a dictionary per structure such as this
can be constructed:
{"task": "\n    Write a function called multiply() in the rust language,
\n    such that given input(s) are (a, b, c),
\n    so, def multiply(a, b, c):
\n    and the output is Multiply three float numbers. Get the product of three float inputs.
\n    ",
"function_name": "multiply",
"input_parameters": ["a", "b", "c"],
"output_description": "Multiply three float numbers. Get the product of three float inputs.",
"test_cases": [
  {"input": [4.0, 5.0, 2.0], "expected_output": 40.0},
  {"input": [3.5, 2.0, 1.5], "expected_output": 10.5},
  {"input": [2.0, 2.0, 2.0], "expected_output": 8.0},
  {"input": [1.0, 1.0, 1.0], "expected_output": 1.0}],
  "programming_language": "rust"}



idea:
project pool...not separate arrays?


8. make a function to produce unit-test outcomes
9. make unit tests
10. make puzzle-json

(final results array...8x8?)

note: maybe not do exponents because of number explosion


The first time you go through, you will see what what the
array sizes will be,
after that you can


append or replace...
can only replace if item exists

first: append


first step:
- starting array
- first role
- first action
- first destination
- append only
-


"""

import random
import sys
from pprint import pprint
import math
import numpy as np
import copy
import json

SEED = 42


##############################
# two indices type operations
##############################
two_indices_type_functions_list = [
    "bitwise_and",
    "bitwise_or",
    "bitwise_xor",
    "addition",
    "subtraction",
    "multiplication",
]

# Bitwise AND
def bitwise_and(x, y):
    return x & y


# Bitwise OR
def bitwise_or(x, y):
    return x | y


# Bitwise XOR
def bitwise_xor(x, y):
    return x ^ y


# addition
def addition(x, y):
    return x + y


# subtraction
def subtraction(x, y):
    return x - y


# multiplication
def multiplication(x, y):
    return x * y


############################
# one index type operations
# for any possible value
# in an array
############################
"""
These functions can handle a wide range of input values, including zero, negatives, and floats, without any specific constraints on the input range.
"""



# List of function names
one_index_type_functions_list = [
    "identity",
    "square",
    "cube",
    "absolute_value",
    "sign",
    "reverse_sign",
    "round_number",
    "floor",
    "ceiling",
    # "log",
    # "log10",
    # "exp",
    # "sqrt",
    "sin",
    "cos",
    "tan",
    # "asin",
    # "acos",
    # "atan",
    # "sinh",
    # "cosh",
    "tanh",
    # "asinh",
    # "acosh",
    # "atanh",
    "degrees_to_radians",
    "radians_to_degrees",
    "conjugate",
    "abs_complex",
    "arg_complex",
    "real_complex",
    "imag_complex",
    "bitwise_not",
    "bitwise_left_shift",
    "bitwise_right_shift_logical",
    "bitwise_right_shift_arithmetic",
]


# Bitwise NOT
def bitwise_not(x):
    """
    The function takes a single argument x, which can be an integer,
    a NumPy array, or any other numeric data type that supports
    bitwise operations.
    Inside the function, the np.bitwise_not() function from the
    NumPy library is called, which performs the
    bitwise NOT operation on the input value x.
    The result of the bitwise NOT operation is returned by the function.
    """
    return np.bitwise_not(x)


# Bitwise left shift
def bitwise_left_shift(x, y=1):
    return np.left_shift(x, y)


# Bitwise right shift (logical)
def bitwise_right_shift_logical(x, y=1):
    return np.right_shift(x, y)


# Bitwise right shift (arithmetic)
def bitwise_right_shift_arithmetic(x, y=1):
    # Convert x to a NumPy array with a data type that can accommodate large values
    x_arr = np.array(x, dtype=np.int64)
    return np.right_shift(x_arr, y)


# Identity function
def identity(x):
    return x


# Square function
def square(x):
    return x ** 2


# Cube function
def cube(x):
    return x ** 3


# Absolute value function
def absolute_value(x):
    return abs(x)


# Sign function
def sign(x):
    return np.sign(x)


# reverse_sign function
def reverse_sign(x):
    return x*-1


# Round function
def round_number(x):
    return np.round(x)


# Floor function
def floor(x):
    return np.floor(x)


# Ceiling function
def ceiling(x):
    return np.ceil(x)


# # Natural logarithm

# def log(x):

#     return np.log(x)


# # Logarithm base 10

# def log10(x):

#     return np.log10(x)


# # Exponential function

# def exp(x):

#     return np.exp(x)


# # Square root function

# def sqrt(x):

#     return np.sqrt(x)


# Trigonometric functions
def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def tan(x):
    return np.tan(x)


# def asin(x):

#     return np.arcsin(x)


# def acos(x):

#     return np.arccos(x)


# def atan(x):

#     return np.arctan(x)


# # Hyperbolic functions

# def sinh(x):

#     return np.sinh(x)


# def cosh(x):

#     return np.cosh(x)

def tanh(x):
    return np.tanh(x)


# def asinh(x):

#     return np.arcsinh(x)


# def acosh(x):

#     return np.arccosh(x)


# def atanh(x):

#     return np.arctanh(x)


# Convert degrees to radians
def degrees_to_radians(degrees):
    return np.radians(degrees)


# Convert radians to degrees
def radians_to_degrees(radians):
    return np.degrees(radians)


# Complex conjugate
def conjugate(x):
    return np.conjugate(x)


# Complex absolute value
def abs_complex(x):
    return np.abs(x)


# Complex argument
def arg_complex(x):
    return np.angle(x)


# Real part of a complex number
def real_complex(x):
    return np.real(x)


# Imaginary part of a complex number
def imag_complex(x):
    return np.imag(x)


def process_single_index_operation(original_array, source_index, processing_function):
    """
    This function takes an array, an index, and a processing function,
    applies the processing function to the value at the specified index in the array,
    and appends the result to a result array.

    :param original_array: the array to process
    :param index: the index of the value to process in the array
    :param processing_function: the function to apply to the value
    :param result_array: the array to append the processed value to
    :return: the original array and the result array
    """
    print(f""" process_single_index_operation()
    inputs

    original_array      -> {original_array}
    source_index        -> {source_index}
    processing_function -> {processing_function}
    """)

    # make safe copy of original array
    copy_of_originalarray = original_array.copy()

    # Look up the function by its name
    function = globals()[processing_function]

    # Get the value at the specified index in the original array
    value = copy_of_originalarray[source_index]

    # Apply the processing function to the value
    result = function(value)

    # Return result
    return result


# helper function for creating json test body
def create_task_description(programming_language, complete_natural_language_project_outline, r_number_of_roles, t_number_of_turns):
    """
    works along with:
    - 
    - create_test_cases

    sample use:
        json_body = create_json_body(
            programming_language, 
            complete_natural_language_project_outline, 
            test_cases, 
            r_number_of_roles, 
            t_number_of_turns)
    """
    task_description = f"""Write one or more functions in the {programming_language} language, 
with the main function called project_tasks_puzzle() 
where the input is a starting array, 
and the needed output is the final ending array 
after the following project schedule process, 
so, def project_tasks_puzzle([array]): is the main function 
and the output is one array of values. 

This is a sequential turn-based project where participants 
perform tasks changing values in arrays. 
Feeding into the final ending array of results 
there is a starting array (the one input parameter) and 
each participant has workspace array. 
There are {r_number_of_roles} roles or participants. 
Each participant has {t_number_of_turns} tasks. 
This is the project operation schedule: 
{complete_natural_language_project_outline}"""

    # remove newlines
    task_description = task_description.replace("\n",'')

    return task_description


# helper function for creating json test body
import numpy as np

def create_test_cases(test_cases):
    """
    works along with:
    - create_task_description
    - create_json_body

    sample use:
        json_body = create_json_body(
            programming_language, 
            complete_natural_language_project_outline, 
            test_cases, 
            r_number_of_roles, 
            t_number_of_turns)
    """
    formatted_test_cases = []
    for test_case in test_cases:
        input_value = test_case["input"]
        expected_output = test_case["expected_output"]
        
        # Convert NumPy data types to Python built-in data types
        input_value = [int(x) for x in input_value]
        expected_output = [int(x) for x in expected_output]
        
        formatted_test_case = {
            "input": input_value,
            "expected_output": expected_output
        }
        formatted_test_cases.append(formatted_test_case)
    return formatted_test_cases
# def create_test_cases(test_cases):
#     """
#     works along with:
#     - create_task_description
#     - create_json_body

#     sample use:
#         json_body = create_json_body(
#             programming_language, 
#             complete_natural_language_project_outline, 
#             test_cases, 
#             r_number_of_roles, 
#             t_number_of_turns)
#     """
#     formatted_test_cases = []
#     for test_case in test_cases:
#         input_value = test_case["input"]
#         expected_output = test_case["expected_output"]
#         formatted_test_case = {
#             "input": input_value,
#             "expected_output": expected_output
#         }
#         formatted_test_cases.append(formatted_test_case)
#     return formatted_test_cases


# helper function for creating json test body
def create_json_body(programming_language, complete_natural_language_project_outline, test_cases, r_number_of_roles, t_number_of_turns):
    """
    works along with:
    - create_task_description
    - create_test_cases

    sample use:
        json_body = create_json_body(
            programming_language, 
            complete_natural_language_project_outline, 
            test_cases, 
            r_number_of_roles, 
            t_number_of_turns)
    """
    task_description = create_task_description(programming_language, complete_natural_language_project_outline, r_number_of_roles, t_number_of_turns)
    formatted_test_cases = create_test_cases(test_cases)
    json_body = {
        "task": task_description,
        "function_name": "project_tasks_puzzle",
        "input_parameters": ["one array of values"],
        "output_description": "The final array of project results",
        "test_cases": formatted_test_cases
    }
    return json_body


def generate_random_starting_array(starting_arraylength_n, decimal_digits=0, allow_negative_numbers=False, power_of_ten_scale=1):
    """
    Generates a random array of numbers with a length of n, optional decimal digits, and optional negative numbers.

    Args:
        starting_arraylength_n (int): The desired length of the array.
        decimal_digits (int): The number of decimal digits to include in the array values. Default is 0.
        allow_negative_numbers (bool): If True, the array can contain negative numbers. Default is False.
        power_of_ten_scale (int): The power of 10 scale for the values. Default is 1 (no scaling).

    Returns:
        list: A list of n random numbers with the specified number of decimal digits and scaling.

    use example:
        array_length = 10
        decimal_digits = 2
        allow_negative_numbers = False
        power_of_ten_scale = 3
        random_array = generate_random_starting_array(array_length, decimal_digits, allow_negative_numbers, power_of_ten_scale)
        print(random_array)
    """
    multiplier = 10 ** decimal_digits

    random_range = 9 * multiplier * (10 ** power_of_ten_scale)

    if allow_negative_numbers:
        random_range *= 2
        random_offset = -random_range // 2
    else:
        random_offset = 0

    if decimal_digits == 0:
        return [round((random.randint(0, random_range) + random_offset)) for _ in range(starting_arraylength_n)]
    else:
        return [round((random.randint(0, random_range) + random_offset) / multiplier, decimal_digits) for _ in range(starting_arraylength_n)]


def process_and_append_two_indices_operation(original_array, index1, index2, processing_function):
    """
    This function takes an array, two indices, and a processing function,
    applies the processing function to the values at the two specified indices in the array,
    and appends the result to a result array.

    :param original_array: the array to process
    :param index1: the index of the first value to process in the array
    :param index2: the index of the second value to process in the array
    :param processing_function: the function to apply to the values
    :param result_array: the array to append the processed value to
    :return: the original array and the result array
    """
    print(f"""1st print process_and_append_two_indices_operation()
    inputs

    original_array      -> {original_array}
    index1              -> {index1}
    index2              -> {index2}
    processing_function -> {processing_function}
    """)

    # Look up the function by its name
    processing_function = globals()[processing_function]

    # Get the values at the specified indices in the original array
    value1 = original_array[index1]
    value2 = original_array[index2]

    # Apply the processing function to the values
    result = processing_function(value1, value2)

    print(f"""2nd print process_and_append_two_indices_operation()
    inputs

    original_array      -> {original_array}
    index1              -> {index1}
    index2              -> {index2}
    processing_function -> {processing_function}

    "result"   -> {result}
    """)

    # Return result
    return result


def two_target_operation_execute(a, b, operation_name):
    """
    Generates a random two-target operation on the given values a and b.
    Returns a tuple containing the operation name and the result.
    """
    operations_dict = {
        'addition': lambda x, y: x + y,
        'subtraction': lambda x, y: x - y if y < x else y - x,
        'multiplication': lambda x, y: x * y,
        # ("raise the first number to the power of the second number for", lambda x, y: x ** y,
        # Add more two-target operations as needed
    }
    operation_name, operation_func = operations_dict(operation_name)
    return operation_name, operation_func(a, b)


"""
Step 3
deterministically make a list of unique ids or roles
such that they are always the same for a given number of roles
"""
def make_role_id_list(r_number_of_roles, random_seed=False, use_random=False):
    """
    deterministically make a list of N unique role-names (or role 'id's)

    """
    print(f"random_seed -> {random_seed}")
    if random_seed:
      print(f"Setting random seed -> {random_seed}")
      # Set a random seed
      random.seed(SEED)

    else:
      # Deactivate the seed
      random.seed()

    role_id_list = []

    # Generate sequential names
    base_names = ["Alice", "Bob", "Cedric", "Doris", "Evelyn", "Frank", "George", "Harry",
                  "Iago", "James", "Kelvin", "LoopinIII", "Moody", "Norbert", "Optimus",
                  "Portus", "Quill", "Ralph", "Serius", "Tom", "Upton", "Vertigo",
                  "Wednesday", "Xrayeyes", "Yetty", "Zookeeper"]

    for i in range(r_number_of_roles):
        index = i % len(base_names)
        suffix = "" if i < len(base_names) else str(i // len(base_names) + 1)
        role_name = base_names[index] + suffix
        role_id_list.append(role_name)

    # randomize role_id_list, if so desired
    if use_random is True:
        random.shuffle(role_id_list)

    return role_id_list


def describe_task(task_dict):
    # Extract the relevant information from the task dictionary
    role = task_dict['role']
    task_blurb = task_dict['task_blurb']
    specific_task_operation = task_dict['specific_task_operation']
    task_source = task_dict['task_source']
    task_sink = task_dict['task_sink']
    operation_source_index_or_slice = task_dict['operation_source_index_or_slice']

    # Construct the paragraph
    paragraph = f"{role} is going to {task_blurb} the '{specific_task_operation}' operation on the data from '{task_source}' and store the result in '{task_sink}'."

    # Handle the different types of operations
    if task_dict['task_type'] == 'one_index_type_operation':
        paragraph += f" The operation will be performed on the element at index {operation_source_index_or_slice}."
    elif task_dict['task_type'] == 'one_slice_type_operation':
        paragraph += f" The operation will be performed on the slice from index {operation_source_index_or_slice[0]} to (but not including) index {operation_source_index_or_slice[1]}."
    elif task_dict['task_type'] == 'two_indices_type_operation':
        paragraph += f" The operation will be performed on the elements at indices {operation_source_index_or_slice[0]} and {operation_source_index_or_slice[1]}."

    return paragraph


def make_turn_data_list(role_id_list,t_number_of_turns, random_seed=False):
    """
    This should make a turn-list, a randomized list
    of which role acts on which turn.
    where the number of turns is the number of roles * number of tasks
    """
    print(f"random_seed -> {random_seed}")
    if random_seed:
      print(f"Setting random seed -> {random_seed}")
      # Set a random seed
      random.seed(SEED)

    else:
      # Deactivate the seed
      random.seed()

    # Make a turn-list, a randomized list of which role acts on which turn
    turn_list = role_id_list * t_number_of_turns

    # Randomize list
    random.shuffle(turn_list)

    return turn_list


def copy_forward_initial_values__workspace_updater(master_list_of_dicts, the_index_to_copy_forward):
    """
    This function takes a list of dictionaries and an index as input. It copies the entire dictionary
    from the given index to the next index in the list.

    Args:
        master_list_of_dicts (list): A list of dictionaries, where each dictionary has the keys 'Alice', 'Bob', 'end_result_project_array', and 'start_project_array'.
        the_index_to_copy_forward (int): The index of the dictionary to be copied.

    Returns:
        None

    details:
    This copies the ENTIRE dictionary. The dictionary IS the 'item' at the index.
    """
    print("starting copy_forward_initial_values__workspace_updater()")

    # Check if the index is valid
    if the_index_to_copy_forward < 0 or the_index_to_copy_forward >= len(master_list_of_dicts) - 1:
        print("Invalid index. Please provide a valid index within the range of the list.")
        print(f"""
        master_list_of_dicts      -> {master_list_of_dicts}
        the_index_to_copy_forward -> {the_index_to_copy_forward}
        """)
        return

    # Get the source dictionary to be copied
    source_dict = master_list_of_dicts[the_index_to_copy_forward]

    # Print the source dictionary for inspection
    print("before copy_forward_initial_values__workspace_updater() ->")
    print("Source dictionary:")
    print(source_dict)

    # Copy the entire source dictionary to the next index in the list
    master_list_of_dicts[the_index_to_copy_forward + 1] = copy.deepcopy(source_dict)

    # Print the updated dictionaries for inspection
    print("After / end of copy_forward_initial_values__workspace_updater() ->")
    print("results of copy_forward_initial_values__workspace_updater() ->")
    print("Source dictionary:")
    print(source_dict)
    print("Target dictionary:")
    print(master_list_of_dicts[the_index_to_copy_forward + 1])
    print("\n")


def make_workspaces_actual_write_to_schedule(workspaces_are_open_to_write_to_schedule):
    """
    Make a workspaces_actual_write_to_schedule:
    You have: an array of arrays of options
    You need: an array of actuals

    Make template
    iterate through options
    pick random options
    append those to list of actuals

    return list of actuals
    """

    workspaces_actual_write_to_schedule = []

    for this_sublist in workspaces_are_open_to_write_to_schedule:
        write_to_here = random.choice(this_sublist)
        workspaces_actual_write_to_schedule.append(write_to_here)

    return workspaces_actual_write_to_schedule


def make_schedule_of_nonempty_workspaces(workspaces_actual_write_to_schedule):
    """
    Make a schedule_of_nonempty_workspaces:
    You have: workspaces_actual_write_to_schedule
    You need: an array of schedule_of_nonempty_workspaces

    process:
    Make a set of available workspaces (non-empty)
    - start with start_project_array,

    There is a time-lag where something written on the LAST
    turn, becomes avaiable on the NEXT turn after that.

    - Each turn, use the set that exists before that turn,
    THEN:

    - add what has been written to (from input array)
    as being no longer empty for and following that turn

    return schedule_of_nonempty_workspaces
    """

    # initialize set of non-empty workspaces
    set_of_existing_non_empty_workspaces = set()

    # add 'start_project_array' to set of of non-empty workspaces
    set_of_existing_non_empty_workspaces.add('start_project_array')

    # initialize output
    schedule_of_nonempty_workspaces = []

    # iterate through input: list of sinks: what arrays are written to
    for name_of_workspace_written_to in workspaces_actual_write_to_schedule:

        # first add set as it existed before this turn
        # add per-turn sub-array -> for this turn: these arrays are not-empty
        schedule_of_nonempty_workspaces.append(list(set_of_existing_non_empty_workspaces))

        # THEN
        # add 'name_of_workspace_written_to' to set THEN non-empty workspaces
        set_of_existing_non_empty_workspaces.add(name_of_workspace_written_to)

    return schedule_of_nonempty_workspaces


def make_nonempty_for_slices_workspace_schedule(workspaces_actual_write_to_schedule, schedule_of_nonempty_workspaces):
    """
    Make a nonempty_for_slices_workspace_schedule, non-empty after two writes
    You have: workspaces_actual_write_to_schedule
    You need: an array of nonempty_for_slices_workspace_schedule

    process:
    Make a set of available workspaces (non-empty)
    - start with start_project_array,

    There is a time-lag where something written on the LAST
    turn, becomes avaiable on the NEXT turn after that.

    - Each turn, use the set that exists before that turn,
    THEN:

    - add what has been written to (from input array)
    as being no longer empty for and following that turn

    return nonempty_for_slices_workspace_schedule


    note: start_array should have more than 1 item inside it
    """

    # initialize set of non-empty workspaces
    set_of_twice_non_empty_workspaces = set()

    # add 'start_project_array' to set of of non-empty workspaces
    set_of_twice_non_empty_workspaces.add('start_project_array')

    # initialize output
    nonempty_for_slices_workspace_schedule = []


    counter = 0

    # iterate through input: list of sinks: what arrays are written to
    for name_of_workspace_written_to in workspaces_actual_write_to_schedule:

        nonempty_for_slices_workspace_schedule.append(list(set_of_twice_non_empty_workspaces))

        # to detect a 2nd write, see if the workspace being written to
        # is already once not-empty
        if name_of_workspace_written_to in schedule_of_nonempty_workspaces[counter]:
            # if so, add that to this new set

            # THEN
            # add 'name_of_workspace_written_to' to set THEN non-empty workspaces
            set_of_twice_non_empty_workspaces.add(name_of_workspace_written_to)

        counter += 1

    return nonempty_for_slices_workspace_schedule


def make_workspaces_are_open_to_write_to_schedule(all_array_workspace_list, turn_data_list):
    """
    Make a workspaces_are_open_to_write_to_schedule:
    you have: A list of roles per turn
    you need: During a turn, which workspaces are open/closed for writing-to?

    To start out:
    Make array of arrays, a list of lists,
    In the overall list, it is a list of turn-data, each 'value' (a list)
    in the list represents, in sequence, that turn.
    Inside that turn-list, the list is a list of which workspaces
    are open to being written to.


    To complete the workspaces_are_open_to_write_to_schedule,
    use the all_array_workspace_list and the turn_data_list:

    overall: see where (on what turn) in the turn_data_list each role's
    last turn is. (and then use that data)

    iterate through the all_array_workspace_list:
    for that role:
        iterate through the turn_data_list, and find where that role
        ends their last turn.

    Using this datum:
    After the turn of that role's last action,
    a.k.a in all turns after that turn in the turn_data_list,
    remove that role-id from the list in workspaces_are_open_to_write_to_schedule
    following that turn.

    Finally:
    ['start_project_array', 'end_result_project_array'],
    During the last phase when no role-workspaces are left,
    also remove the start_project array as a sink.

    Should be -> only ['end_result_project_array']

    """
    workspaces_are_open_to_write_to_schedule = []

    # make last_turn_index
    last_turn_index = {role: None for role in all_array_workspace_list}

    # Find the last turn index for each role
    for i, role in enumerate(turn_data_list):
        if role in last_turn_index and last_turn_index[role] is None:
            last_turn_index[role] = i

    # Create the initial schedule with all workspaces open
    for _ in range(len(turn_data_list)):
        workspaces_are_open_to_write_to_schedule.append(all_array_workspace_list.copy())

    # Close workspaces for roles after their last turn
    for role, last_turn in last_turn_index.items():
        if last_turn is not None:
            for i in range(last_turn + 1, len(turn_data_list)):
                workspaces_are_open_to_write_to_schedule[i].remove(role)

    # Modify the list elements: if only options are: start & end -> only: end
    for i, workspace_list in enumerate(workspaces_are_open_to_write_to_schedule):
        if workspace_list == ['start_project_array', 'end_result_project_array']:
            workspaces_are_open_to_write_to_schedule[i] = ['end_result_project_array']

    return workspaces_are_open_to_write_to_schedule


def make_workspaces_are_open_to_read_from_schedule(all_array_workspace_list, turn_data_list, workspaces_are_open_to_write_to_schedule):
    """
    Make a make_workspaces_are_open_to_read_from_schedule:
    you have:
      - you know the turns
      - you know list of workspaces
      - you know available writes
    you need: During a turn, which workspaces are open/closed for reading from?

    Process:
    using workspaces_are_open_to_write_to_schedule,
    call function to generate an actual to_write_to_schedule.

    Use those values to fill in.



    To complete the make_workspaces_are_open_to_read_from_schedule,
    ...

    overall:
    - you cannot read from an empty array
    - the first read every must be from the start-array
    which is the only array at the start

    Sequence:
    - you know the turns
    - you know list of workspaces
    - you know available writes

    - you need:
    1. a more detailed (maybe incrimental) map of what has been written to
    2. maybe make a second actual-write-to list...random from possible
    2. only read from what has been written to...
    3.


    iterate through the all_array_workspace_list:


    Using this datum:


    Finally:


    """

    # make actaul write-to array
    workspaces_actual_write_to_schedule = make_workspaces_actual_write_to_schedule(workspaces_are_open_to_write_to_schedule)

    make_workspaces_are_open_to_read_from_schedule = []

    # make last_turn_index
    last_turn_index = {role: None for role in all_array_workspace_list}

    # Find the last turn index for each role
    for i, role in enumerate(turn_data_list):
        if role in last_turn_index and last_turn_index[role] is None:
            last_turn_index[role] = i

    # Create the initial schedule with all workspaces open
    for _ in range(len(turn_data_list)):
        make_workspaces_are_open_to_read_from_schedule.append(all_array_workspace_list.copy())

    # Close workspaces for roles after their last turn
    for role, last_turn in last_turn_index.items():
        if last_turn is not None:
            for i in range(last_turn + 1, len(turn_data_list)):
                make_workspaces_are_open_to_read_from_schedule[i].remove(role)

    # Modify the list elements: if only options are: start & end -> only: end
    for i, workspace_list in enumerate(make_workspaces_are_open_to_read_from_schedule):
        if workspace_list == ['start_project_array', 'end_result_project_array']:
            make_workspaces_are_open_to_read_from_schedule[i] = ['end_result_project_array']

    return make_workspaces_are_open_to_read_from_schedule


def add_or_replace_result_at_index(array_name, add_or_replace, index_or_slice, value):
    """
    Adds or replaces a value or values in a list at a specified index or slice.
    Args:
        array_name (list): The list to be modified.
        add_or_replace (str): A string indicating whether to add or replace values.
                              Valid values are 'add' or 'replace'.
        index_or_slice (int or slice or tuple): The index, slice, or tuple representing a slice where the value(s) should be added or replaced.
                                                 Supports standard slice notations like [:2] or [-4:].
        value (any): The value or list of values to be added or replaced.
    Returns:
        list: The modified list.
    """
    if isinstance(index_or_slice, tuple):
        if len(index_or_slice) == 1:
            index_or_slice = index_or_slice[0]
        elif len(index_or_slice) == 2:
            index_or_slice = slice(index_or_slice[0], index_or_slice[1])
        elif len(index_or_slice) == 3:
            index_or_slice = slice(index_or_slice[0], index_or_slice[1], index_or_slice[2])
        else:
            sys.exit("Invalid slice tuple length")

    if add_or_replace.lower() == 'add':
        if isinstance(index_or_slice, int):
            array_name.insert(index_or_slice, value)
        else:
            start = index_or_slice.start if index_or_slice.start is not None else 0
            stop = index_or_slice.stop if index_or_slice.stop is not None else len(array_name)
            step = index_or_slice.step if index_or_slice.step is not None else 1

            # handle multiple values
            if isinstance(value, list):
                print(f"value -> {value}")
                if step == 1:
                    array_name[start:stop:step] = array_name[start:stop:step] + value
                else:
                    for i, this_number in enumerate(value):
                        array_name.insert(start + i * step, this_number)
    elif add_or_replace.lower() == 'replace':
        if isinstance(index_or_slice, int):
            array_name[index_or_slice] = value
        else:
            start = index_or_slice.start if index_or_slice.start is not None else 0
            stop = index_or_slice.stop if index_or_slice.stop is not None else len(array_name)
            step = index_or_slice.step if index_or_slice.step is not None else 1
            array_name[start:stop:step] = value
    else:
        raise ValueError("Invalid value for 'add_or_replace'. Must be 'add' or 'replace'.")

    return array_name


def select_possible_task_type(
    turn,
    task_source,
    one_index_type_functions_list,
    two_indices_type_functions_list,
    schedule_of_nonempty_workspaces,
    nonempty_for_slices_workspace_schedule,
):
    """
    Pick task type based on length of available arrays.
    to have a slice there must be at least two values to slice

    note:
    modes:
    - string
    - int
    - bitwize
    - 8x8 puzzle
    """
    # task_type_list = ["slice_type_operation", "one_index_type_operation", "two_indices_type_operation"]

    if task_source in nonempty_for_slices_workspace_schedule[turn - 1]:
        # if there can be more than one index
        return random.choice(two_indices_type_functions_list)

    else:
        # if only one index exists
        return random.choice(one_index_type_functions_list)




# def array_slice_operation_generator(source_array):
#     """
#     generate a random array slice operation on the given source_array.
#     Returns a tuple containing the operation name, the slice, and the result.

#     This may be a BAD function that tries to do too many
#     tasks rather than doing one thing well.
#     """
#     operations = [
#         ("reverse", lambda x: list(reversed(x))),
#         ("sum", sum),
#         ("product", lambda x: x[0] * x[-1] if len(x) > 1 else x[0]),
#         # Add more array slice operations as needed
#         # add:
#         # sort
#         # reverse sort
#         # make int
#     ]
#     operation_name, operation_func = random.choice(operations)

#     if len(source_array) == 1:
#         print("source_array in array_slice_operation_generator -> ", source_array)
#         return operation_name, source_array, "[0]", operation_func(source_array)
#     else:
#         # Generate random start and end indices for the slice
#         # so that the slice is not one number

#         if len(source_array) < 3:
#             print("input array too short, must be at least length=3")
#             return operation_name, source_array, None, operation_func(source_array)

#         slice_ok_flag = False
#         while not slice_ok_flag:
#             start = random.randint(0, len(source_array) - 2)
#             end = random.randint(start + 1, len(source_array))

#             if (end - start) > 1:
#                 slice_ok_flag = True
#             else:
#                 print("too short of a slice")

#         # return the values of the slices array
#         slice_array = source_array[start:end]


#         # return the indices of the slice:
#         slice_indices = f"[{start}:{end}]"


#         return operation_name, slice_array, slice_indices, operation_func(slice_array)




# def two_target_operation_generator(a, b):
#     """
#     Generates a random two-target operation on the given values a and b.
#     Returns a tuple containing the operation name and the result.
#     """
#     operations = [
#         ("perform addition on", lambda x, y: x + y),
#         ("perform subtraction on", lambda x, y: x - y if y < x else y - x),
#         ("perform multiplication on", lambda x, y: x * y),
#         ("raise the first number to the power of the second number for", lambda x, y: x ** y),
#         # Add more two-target operations as needed
#     ]
#     operation_name, operation_func = random.choice(operations)
#     return operation_name, operation_func(a, b)


def slice_operation_generator():
    """
    returns: blurb, operation_name
    Generates a random two-target operation on the given values a and b.
    Returns a tuple containing the operation name and the result.
    """
    operations = [
        ("perform reverse on", 'reverse'),
        ("get sum of", 'sum'),
        ("get product of", 'product'),
        ("perform sort on", 'sort'),
        ("perform reverse-sort on", 'reverse_sort'),
        ("make an integer from", "make_int")
        # ("raise the first number to the power of the second number for", lambda x, y: x ** y),
        # Add more two-target operations as needed
    ]
    blurb, operation_name = random.choice(operations)
    return blurb, operation_name


def two_target_operation_generator():
    """
    returns: blurb, operation_name
    Generates a random two-target operation on the given values a and b.
    Returns a tuple containing the operation name and the result.
    """
    operations = [
        ("perform addition on", 'addition'),
        ("perform subtraction on", 'subtraction'),
        ("perform multiplication on", 'multiplication'),
        ("perform bitwise_and on", 'bitwise_and'),
        ("perform bitwise_or on", 'bitwise_or'),
        ("perform bitwise_xor on", 'bitwise_xor'),

        # ("raise the first number to the power of the second number for", lambda x, y: x ** y),
        # Add more two-target operations as needed
    ]
    blurb, operation_name = random.choice(operations)
    return blurb, operation_name


def one_target_operation_generator():
    """
    returns: blurb, operation_name
    Generates a random two-target operation on the given values a and b.
    Returns a tuple containing the operation name and the result.

    """
    operations = [
        ("apply the identity function to", "identity"),
        ("apply the square function to", "square"),
        ("apply the cube function to", "cube"),
        ("apply the absolute value function to", "absolute_value"),
        ("apply the sign function to", "sign"),
        ("apply the reverse sign function to", "reverse_sign"),
        ("apply the round number function to", "round_number"),
        ("apply the floor function to", "floor"),
        ("apply the ceiling function to", "ceiling"),
        ("apply the sine function to", "sin"),
        ("apply the cosine function to", "cos"),
        ("apply the tangent function to", "tan"),
        ("apply the hyperbolic tangent function to", "tanh"),
        ("convert degrees to radians for", "degrees_to_radians"),
        ("convert radians to degrees for", "radians_to_degrees"),
        ("apply the conjugate function to", "conjugate"),
        ("apply the absolute value function to a complex number", "abs_complex"),
        ("apply the argument function to a complex number", "arg_complex"),
        ("extract the real part of a complex number", "real_complex"),
        ("extract the imaginary part of a complex number", "imag_complex"),
        ("apply the bitwise NOT operation to", "bitwise_not"),
        ("apply the bitwise left shift operation to", "bitwise_left_shift"),
        ("apply the bitwise right shift (logical) operation to", "bitwise_right_shift_logical"),
        ("apply the bitwise right shift (arithmetic) operation to", "bitwise_right_shift_arithmetic"),
    ]
    blurb, operation_name = random.choice(operations)
    return blurb, operation_name


def move_array_value_two_arrays():
    # todo
    pass

def one_target_bitwise_operation_generator():
    # todo
    pass


def relocate_value_to_random_empty_location(original_array, index, result_array):
    """
    This function takes an 8x8 array, an index, and an 8x8 result array.
    It relocates the value at the specified index in the original array to a random empty location in the result array.
    If the index is out of range for the original array, it does not modify the result array.

    :param original_array: the 8x8 array to process
    :param index: the index of the value to relocate in the original array
    :param result_array: the 8x8 array to relocate the value to
    :return: the original array and the modified result array
    """


    # Check if the index is within the bounds of the original array
    if index < 0 or index >= len(original_array) * len(original_array[0]):
        return original_array, result_array

    # Get the value at the specified index in the original array
    row = index // len(original_array[0])
    col = index % len(original_array[0])
    value = original_array[row][col]


    # Get the value at the specified index in the original array
    original_array[row][col] = None

    # Find an empty location in the result array
    empty_locations = [(i, j) for i in range(8) for j in range(8) if result_array[i][j] == None]
    if empty_locations:
        row, col = random.choice(empty_locations)
        result_array[row][col] = value

    # Return the original array and the modified result array
    return original_array, result_array


# for 8x8 puzzles
def relocate_random_value_to_random_empty_location(original_array, result_array):
    """
    This function takes an 8x8 array and an 8x8 result array.
    It relocates a random not-None value from the original array to a random empty location in the result array.

    :param original_array: the 8x8 array to process
    :param result_array: the 8x8 array to relocate the value to
    :return: the modified original array and the modified result array
    """
    # Get the indices of not-None values in the original array
    not_none_indices = [(i, j) for i in range(8) for j in range(8) if original_array[i][j] is not None]

    # If there are no not-None values, return the original arrays
    if not not_none_indices:
        return original_array, result_array

    # Choose a random not-None index
    row, col = random.choice(not_none_indices)
    value = original_array[row][col]

    # Set the chosen value to None in the original array
    original_array[row][col] = None

    # Find an empty location in the result array
    empty_locations = [(i, j) for i in range(8) for j in range(8) if result_array[i][j] is None]
    if empty_locations:
        row, col = random.choice(empty_locations)
        result_array[row][col] = value

    # Return the modified original array and the modified result array
    return original_array, result_array


def array_slice_operation_executor(operation_name, source_slice_coordinates, array_input):
    """
    Carries out an array slice operation and returns the result

    Args:
        operation_name (str): The name of the operation to perform on the slice.
        source_slice_coordinates (tuple): A tuple containing the start and stop indices for slicing the array.
        array_input (list): The input array.

    Returns:
        The result of the specified operation performed on the slice of the input array.
    """
    print(f"""
    start (before)
    array_slice_operation_executor()

        operation_name           -> {operation_name}
        source_slice_coordinates -> {source_slice_coordinates}
        type of coordiantes      -> {type(source_slice_coordinates)}
        array_input              -> {array_input}

      """)


    operations = {
        "reverse": lambda x: list(reversed(x)),
        "sum": sum,
        "product": lambda x: x[0] * x[-1] if len(x) > 1 else (x[0] if x else None),
        "sort": lambda x: sorted(x),
        "reverse_sort": lambda x: sorted(x, reverse=True),
        "make_int": lambda x: [int(float(item)) for item in x]
    }

    if operation_name not in operations:
        raise ValueError(f"Invalid operation name: {operation_name}")

    start, stop = source_slice_coordinates
    array_slice = array_input[start:stop]
    operation = operations[operation_name]
    result = operation(array_slice)

    print(f"""
    end (after)
    array_slice_operation_executor()

        operation_name    -> {operation_name}
        source_slice_coordinates -> {source_slice_coordinates}
        array_input       -> {array_input}
        operation         -> {operation}
        result            -> {result}
      """)

    return result


# def beta_relocate_value_to_random_empty_location(arrays):
#     """
#     This function takes a list of 8x8 arrays and relocates a value from one array
#     to a random empty location in another random array.

#     :param arrays: a list of 8x8 arrays
#     :return: the modified list of arrays
#     """
#     # Choose a random array from the list
#     source_array = random.choice(arrays)

#     # Find a non-empty location in the source array
#     non_empty_locations = [(i, j) for i in range(8) for j in range(8) if source_array[i][j] != 0]
#     if not non_empty_locations:
#         return arrays  # All arrays are empty, no relocation possible

#     # Choose a random non-empty location in the source array
#     source_row, source_col = random.choice(non_empty_locations)
#     value_to_relocate = source_array[source_row][source_col]

#     # Choose a random array from the list (excluding the source array)
#     target_arrays = [arr for arr in arrays if arr is not source_array]
#     target_array = random.choice(target_arrays)

#     # Find an empty location in the target array
#     empty_locations = [(i, j) for i in range(8) for j in range(8) if target_array[i][j] == 0]
#     if not empty_locations:
#         return arrays  # Target array is full, no relocation possible

#     # Choose a random empty location in the target array
#     target_row, target_col = random.choice(empty_locations)

#     # Relocate the value
#     source_array[source_row][source_col] = 0
#     target_array[target_row][target_col] = value_to_relocate

#     # Replace the modified arrays in the list
#     modified_arrays = [arr if arr is not source_array and arr is not target_array else arr[:] for arr in arrays]
#     modified_arrays[arrays.index(source_array)] = source_array
#     modified_arrays[arrays.index(target_array)] = target_array

#     return modified_arrays




# def two_target_operation_execute(a, b, operation_name):
#     """
#     Generates a random two-target operation on the given values a and b.
#     Returns a tuple containing the operation name and the result.
#     """
#     operations_dict = {
#         'addition': lambda x, y: x + y,
#         'subtraction': lambda x, y: x - y if y < x else y - x,
#         'multiplication': lambda x, y: x * y,
#         # ("raise the first number to the power of the second number for", lambda x, y: x ** y,
#         # Add more two-target operations as needed
#     }
#     operation_name, operation_func = operations_dict(operation_name)
#     return operation_name, operation_func(a, b)



# def outline_task_schedule(r_number_of_roles, t_number_of_turns, random_seed=False):

#     skeleton_schedule = make_skeleton_schedule(start_project_array, r_number_of_roles, t_number_of_turns, random_seed=False)

#     # make array to store workspace-array values



#     return skeleton_schedule


# def generate_task(participant_id, task_number, project_array, final_results_array, participant_arrays, participant_names):
#     task_type = random.choice(["array_slice", "two_target"])
#     target_array = None



#     if task_type == "array_slice":
#         # Select a non-empty array from project_array and participant_arrays
#         non_empty_arrays = [arr for arr in [project_array] + participant_arrays if len(arr) > 0]
#         if not non_empty_arrays:
#             raise ValueError("No non-empty arrays available for array slice operation.")
#         source_array = random.choice(non_empty_arrays)
#         operation_name, slice_array, slice_indices, result = array_slice_operation_generator(source_array)

#         # Generate the task description based on the source array, slice, and operation
#         if source_array == project_array:
#             array_name = "the project input array"
#         else:
#             participant_index = participant_arrays.index(source_array)
#             array_name = f"a participant's array (participant {participant_names[participant_index]})"
#         task = f"For {participant_id}, task {task_number} is to {operation_name} the slice {slice_indices} of {array_name}."

#         # Append the result to the final results array
#         final_results_array.append(result)
#         task += f"\n{participant_id} appends the result to the final results array."

#     else:
#         target_arrays = [project_array] + participant_arrays
#         # Check if there are any valid target arrays
#         if not target_arrays:
#             # If no valid target arrays, fall back to using project_array
#             target_arrays = [project_array]
#         ok_flag = False
#         while not ok_flag:
#             a_array = random.choice(target_arrays)
#             b_array = random.choice(target_arrays)


#             # index needed
#             # Pick a random index for a_array
#             if a_array:
#                 a_index = random.randint(0, len(a_array) - 1)
#                 a = a_array[a_index]
#             else:
#                 a_index = None
#                 a = None

#             # Pick a random index for b_array
#             if b_array:
#                 b_index = random.randint(0, len(b_array) - 1)
#                 b = b_array[b_index]
#             else:
#                 b_index = None
#                 b = None

#             # If both a and b exist, proceed with the operation
#             if a and b:
#                 ok_flag = True
#                 operation_name, result = two_target_operation_generator(a, b)
#                 # Generate the task description based on the chosen elements and operation
#                 a_array_name = "project input array" if a_array == project_array else f"array of participant {participant_names[participant_arrays.index(a_array)]}"
#                 b_array_name = "project input array" if b_array == project_array else f"array of participant {participant_names[participant_arrays.index(b_array)]}"
#                 task = f"For {participant_id}, task {task_number} is to {operation_name} the contents of index {a_index} in the {a_array_name}array, and the contents of index {b_index} in the {b_array_name}."
#         # Randomly choose the target array for appending the result
#         target_array = random.choice([project_array] + participant_arrays)
#         target_array_index = participant_arrays.index(target_array) if target_array in participant_arrays else -1
#         target_array_name = "the project input array" if target_array == project_array else f"a participant's array (array of participant/role {participant_names[target_array_index]})"
#         task += f"\n{participant_id} appends the result to {target_array_name}."
#     return task, result, target_array


# def generate_task_tree(participants, tasks_per_participant, project_array):
#     participant_names = ["Alice", "Bob", "Calvin", "Doris", "Evelyn", "Frank", "Grace", "Henry", "Ivy", "Jack"][:participants]
#     task_tree = []
#     participant_arrays = [[] for _ in range(participants)]
#     final_results_array = []

#     for i in range(tasks_per_participant):
#         for j, participant in enumerate(participant_names):
#             task, result, target_array = generate_task(participant, i + 1, project_array, final_results_array, participant_arrays, participant_names)
#             task_tree.append((participant, task, result, target_array))
#             if target_array is not None:
#                 target_array.append(result)

#     print(f"task_tree -> {task_tree}")
#     print(f"final_results_array -> {final_results_array}")

#     return task_tree, final_results_array


# def generate_project_schedule(participants, tasks_per_participant, project_array):
#     task_tree, final_results_array = generate_task_tree(participants, tasks_per_participant, project_array)
#     tasks = [task for _, task, _, _ in task_tree]

#     question = "Task & Instructions: \n"
#     question += f"Given the project-workflow-description below, \n"
#     question += "produce a function that accepts an array of values as input, \n and produces a correct project outcome array.\n"
#     if tasks_per_participant == 1:
#         question += f"In a project with {participants} participants, where each participant has {tasks_per_participant} task, \n"
#     else:
#         question += f"In a project with {participants} participants, where each participant has {tasks_per_participant} tasks, \n"
#     question += f"where the starting values are in the input project-array, \n the tasks are:\n"
#     question += "\n".join(tasks)
#     question += "\nOutput an array containing the result value or values."

#     return question, final_results_array


# def array_slice_or_two_index_finder(source_array):
#     """
#     Generate a random slice from the given source_array.
#     Returns the values of the slice.
#     """
#     print(f"source_array -> {source_array}")
#     array_length = len(source_array)

#     if len(source_array) < 2:
#         print(f"Input array too short, must be at least length=3, len(source_array) -> {len(source_array)}")
#         return None

#     slice_ok_flag = False
#     while not slice_ok_flag:
#         start = random.randint(-array_length, len(source_array) - 2)
#         end = random.randint(-array_length + 1, len(source_array))

#         # make slice of more than one value
#         if (len(source_array[start:end])) > 1:
#             slice_ok_flag = True
#         else:
#             print("Failed-attempt, Too short of a slice")
#             pass


#     print(f"start -> {start}")
#     print(f"end -> {end}")

#     slice_coordinates_tuple = (start, end)
#     index_values_tuple = (source_array[start], source_array[end])
#     slice_values = source_array[start:end]
#     return slice_coordinates_tuple, index_values_tuple, slice_values


# def array_slice_or_two_index_finder(source_array):
#     """
#     Generate a random slice from the given source_array.
#     Returns the values of the slice.
#     """
#     print(f"source_array -> {source_array}")
#     array_length = len(source_array)

#     if array_length < 3:
#         print(f"Input array too short, must be at least length=3, len(source_array) -> {len(source_array)}")
#         return None

#     slice_ok_flag = False
#     while not slice_ok_flag:
#         start = random.randint(0, array_length - 2)
#         end = random.randint(start + 2, array_length)

#         # make slice of more than one value
#         if (len(source_array[start:end])) > 1:
#             slice_ok_flag = True
#         else:
#             print("Failed-attempt, Too short of a slice")

#     print(f"start -> {start}")
#     print(f"end -> {end}")

#     slice_coordinates_tuple = (start, end)
#     index_values_tuple = (source_array[start], source_array[end - 1])
#     slice_values = source_array[start:end]
#     return slice_coordinates_tuple, index_values_tuple, slice_values


def array_two_index_finder_index_maker(source_array):
    """
    Generate two random indices from the given source_array.
    Returns the values at those indices.
    """
    print(f"array_two_index_finder_index_maker source_array -> {source_array}")
    array_length = len(source_array)

    if array_length < 2:
        print(f"Input array too short, must be at least length=2, len(source_array) -> {len(source_array)}")
        return None

    index1 = random.randint(0, array_length - 1)
    index2 = random.randint(0, array_length - 1)
    while index2 == index1:
        index2 = random.randint(0, array_length - 1)

    print(f"index1 -> {index1}")
    print(f"index2 -> {index2}")

    index_coordinates_tuple = (index1, index2)
    # values_tuple = (source_array[index1], source_array[index2])

    print(f"returning: index_coordinates_tuple -> {index_coordinates_tuple}")
    # print(f"values_tuple -> {values_tuple}")
    return index_coordinates_tuple  #, values_tuple


def array_two_value_finder(source_array, values_tuple):
    print(f"array_two_value_finder()")
    print(f"source_array -> {source_array}")
    print(f"values_tuple -> {values_tuple}")

    index1 = values_tuple[0]
    index2 = values_tuple[1]
    values_tuple = (source_array[index1], source_array[index2])

    return values_tuple


def valid_single_index_finder_index_maker(source_array):
    """
    return a valid index for the input array
    """
    print("starting valid_single_index_finder_index_maker()")
    if not source_array:
        print("array empty in valid_single_index_finder_index_maker()")

    array_length = len(source_array)
    valid_index = random.randint(0, array_length - 1)
    # value_at_index = source_array[valid_index]

    return valid_index  #, value_at_index


def one_array_single_value_finder(source_array, valid_index):
    print("\nStarting: one_array_single_value_finder()")
    print(f"source_array -> {source_array}")
    print(f"valid_index -> {valid_index}\n")

    value_at_index = source_array[valid_index]

    return value_at_index


def array_slice_finder_index_maker(source_array):
    """
    Generate a random slice from the given source_array.
    Returns the values of the slice.
    """
    print(f"source_array -> {source_array}")
    array_length = len(source_array)

    min_length = 2
    if array_length < min_length:
        print(f"Input array too short, must be at least length={min_length}, len(source_array) -> {len(source_array)}")
        sys.exit()

    slice_ok_flag = False
    max_attempts = 10  # Maximum number of attempts to find a valid slice
    attempt_count = 0

    while not slice_ok_flag and attempt_count < max_attempts:
        start = random.randint(0, array_length - 2)
        end = random.randint(start + 1, array_length)

        # Check if the slice coordinates are valid
        if start < end:
            slice_ok_flag = True
        else:
            print("Failed-attempt, Invalid slice coordinates")
            attempt_count += 1

    if not slice_ok_flag:
        print("Failed to find a valid slice after maximum attempts.")
        sys.exit()

    print(f"start -> {start}")
    print(f"end -> {end}")

    slice_coordinates_tuple = (start, end)
    # slice_values = source_array[start:end]
    return slice_coordinates_tuple  #, slice_values


def array_slice_value_finder(source_array, slice_coordinates_tuple):
    start = slice_coordinates_tuple[0]
    end = slice_coordinates_tuple[1]
    slice_values = source_array[start:end]

    return slice_values

def pp_list(this_list):
    """
    pretty print dicts in list
    uses from pprint import pprint
    """
    count_the_pp = 1

    for this_thing_in_the_list in this_list:
        print("\n")
        # print item number
        print(count_the_pp)

        # pretty print the value/element/thing in the list
        pprint(this_thing_in_the_list)

        # increment counter
        count_the_pp += 1

    # final new line
    print("\n")


"""
Steps 4,5
Task schedule skeleton,
- make a structure
- fill in task type
"""
def make_skeleton_schedule(
        r_number_of_roles,
        t_number_of_turns,
        starting_arraylength_n,
        decimal_digits=0,
        allow_negative_numbers=False,
        power_of_ten_scale=1,
        n_unit_tests_to_make=2,
        random_seed=False):
    # TODO
    """
    This should use a turn-list, a randomized list
    of which role acts on which turn.
    where the number of turns is the number of roles * number of tasks

    To make the schedule
    start with a full list of participants in every turn


    Modular plan for task schedule:

    1. get number of roles
    2. get number of tasks
    3. make a list of roles with unique names,
      from alice to zookeeper, then alice1 to zookeeper1, though Alice-N-number to Zookeeper-N-number
    4. make random empty-skeleton schedule of tasks
    5. fill in random task operations
    6. fill in semi-random task inputs, based on existing possible arrays
    which come from a role-array or the start-array.
    7. fill in task outputs such that all 'branches' lead to a final result
    - it is not the last action of each participant,


    But the last action of each participant - (minus) the number of participants.
    a.k.a. The last task, if the tasks are done in role-id- order
    (which they may not be)
    -
    - last "task"
    - you can only read from your own array
    or an array that is complete
    - you can only write to the final results array

    - map of completed roles:
      -
    - note: you can't write to a completed array...

    maybe: you can always input from anywhere
    but you can only output anywhere until while all roles are active
    (not completed), after one role is complete, you can only write
    to your own array or the project array.

    a way to check:
    when you act, what arrays are open?

    workspaces_are_open_to_write_to_schedule:
    During a turn, which workspaces are open/closed for writing-to

    make array of arrays, a list of lists,
    where at the top level each list a turn
    and where inside that turn list the list is a list of which workspaces
    are open to being written to:

    start with a full list of participants in every turn

    to make, use turn sequence:
    for each role, after the turn of that role's last action,
    a.k.a in all turns after that turn,
    remove that role-id from the list of open-workspaces in that turn.
    """

    test_cases_list = []
    complete_natural_language_project_outline = ""

    print(f"random_seed -> {random_seed}")
    if random_seed:
      print(f"Setting random seed -> {random_seed}")
      # Set a random seed
      random.seed(SEED)

    else:
      # Deactivate the seed
      random.seed()

    # # lists maybe longer in future
    # task_type_list = [
    #     "one_slice_type_operation",
    #     # "two_slice_type_operation",
    #     "one_index_type_operation",
    #     "two_indices_type_operation"
    #     ]




    # use function to make role-id-list
    role_id_list = make_role_id_list(r_number_of_roles, random_seed=False, use_random=False)

    # make list of all possible workspaces/arrays
    all_array_workspace_list = role_id_list + ['start_project_array','end_result_project_array']


    # Make a turn-list, a randomized list of which role acts on which turn
    turn_data_list = make_turn_data_list(role_id_list,t_number_of_turns, random_seed=False)

    print(f"\nlen(turn_data_list) -> {len(turn_data_list)}\n")
    print(turn_data_list)
    pprint(turn_data_list)

    workspaces_are_open_to_write_to_schedule = make_workspaces_are_open_to_write_to_schedule(
        all_array_workspace_list,
        turn_data_list)

    # Initialize the schedule tree
    schedule_tree_dict = {}



    """
    todo end_array cannot be source until it is written to
    look at dict
    maybe: first pass: random writes
    based on writes, make open_to_read_schedule
    maybe then add sizes to that?


    option_schedules:

    - options are set for availaiblity per turn
    -

    make workspaces_actual_write_to_schedule

    use that to make an avaiable-to-read-from schedule:
    - if an array has been written to, it can be read from
    -

    note: an array with-only one value, may not be useful for slices...
    - or maybe that would act to move-copy that one value
    -

    using this model:
    random.choice(workspaces_are_open_to_write_to_schedule[turn -1]),

    a prerequisite for slice operation having at least two items in array

    maybe picking specific operation...
    -

    """

    # # make actual write-to array

    workspaces_actual_write_to_schedule = make_workspaces_actual_write_to_schedule(workspaces_are_open_to_write_to_schedule)

    schedule_of_nonempty_workspaces = make_schedule_of_nonempty_workspaces(workspaces_actual_write_to_schedule)

    # TODO: two-idex operations also need this...!!!
    # Q: if you can find two lengths...why not all?
    nonempty_for_slices_workspace_schedule = make_nonempty_for_slices_workspace_schedule(workspaces_actual_write_to_schedule, schedule_of_nonempty_workspaces)


    print(f"schedule_of_nonempty_workspaces -> {schedule_of_nonempty_workspaces}")
    pp_list(schedule_of_nonempty_workspaces)

    print(f"nonempty_for_slices_workspace_schedule -> {nonempty_for_slices_workspace_schedule}")
    pp_list(nonempty_for_slices_workspace_schedule)

    """
    Fill out first parts of schedule:
    on the first pass you can know:
      - turn number
      - id per turn (by choice set to: alphabetical order)
      - task type   (by choice set to: random order)
      - task source, from available sources:  (by choice set to: random order)
      - task_sink, from available sinks:  (by choice set to: random order)

    not yet known
      - operation_source_index_or_slice
      - operation_sink_index_insert


    getting blurb...

    two_target_operation_generator():
        returns: blurb, operation_name

    one index operation...
      - move (as in some 8x8)
    two-index operations...
      -

    """

    one_index_type_functions_list = [
        "one_index_type_operation",
        ]

    two_indices_type_functions_list = [
        "one_slice_type_operation",
        # "two_slice_type_operation",
        "two_indices_type_operation"
        ]

    turn = 1

    # sweep-pass-one
    for this_turn_id in turn_data_list:
        print(f"turn -> {turn}, for this_turn_id")
        print(f"len(turn_data_list) -> {len(turn_data_list)}")

        print(f"schedule_tree_dict -> {schedule_tree_dict}")
        pprint(schedule_tree_dict)

        task_source = random.choice(schedule_of_nonempty_workspaces[turn -1])

        # depends on various factors
        task_type = select_possible_task_type(
            turn,
            task_source,
            one_index_type_functions_list,
            two_indices_type_functions_list,
            schedule_of_nonempty_workspaces,
            nonempty_for_slices_workspace_schedule,
        )
        task_sink = workspaces_actual_write_to_schedule[turn -1]

        if task_type == 'one_slice_type_operation':
            blurb, operation_name = slice_operation_generator()

        elif task_type == 'two_indices_type_operation':
            blurb, operation_name = two_target_operation_generator()

        elif task_type == 'one_index_type_operation':
            blurb, operation_name = one_target_operation_generator()

        else:
            print("Wahhh Huh???")

        schedule_tree_dict[turn] = {
            'role': this_turn_id,
            'task_type': task_type,
            'task_source': task_source,
            'operation_source_index_or_slice': None,  # need to know array length
            'task_sink': task_sink,
            'operation_sink_index_insert': None,  # need to know array length
            'task_blurb': blurb,
            'specific_task_operation': operation_name,
        }
        turn += 1


    print(f"schedule_tree_dict -> {schedule_tree_dict}")
    print("pp-tree")
    pprint(schedule_tree_dict)


    ###################
    ###################
    # fill out details
    ###################
    ###################
    # 2nd sweep
    print("\n\n\nStarting 2nd sweep\n\n\n")
    """
    - add operation_source_index_or_slice
    - perform operation
    - make unit tests
    -
    """

    """
    per_task_to_do__workspaces_values_arrays

    array of turn's taken or tasks done:
    each task-to-do-array is a dict:
    to lookup the workspace[array] for each workspace

    so for each task, there will be a set of all workspaces available
    for that task to act upon, in current state.


    TODO:
    Results:
    updates values are written to the next turn's
    'current' state
    unchanged values are copied as they are
    results update changed workspaces
    """

    per_task_to_do__workspaces_values_arrays = []

    # iterate through each task by each participant/role
    # add one more for the final result
    # for _ in range (len(turn_data_list) + 1):
    #     dict_for_this_turn = {}

    #     for this_workspace in all_array_workspace_list:
    #         dict_for_this_turn[this_workspace] = []

    #     # add that dict or workspaces for this task-to-do
    #     import copy
    #     superfluous_copy_of_dict = copy.deepcopy(dict_for_this_turn)
    #     per_task_to_do__workspaces_values_arrays.append(superfluous_copy_of_dict)

    # iterate through each task by each participant/role
    # add one more for the final result
    for _ in range (len(turn_data_list) + 1):
        dict_for_this_turn = {this_workspace: [] for this_workspace in all_array_workspace_list}
        per_task_to_do__workspaces_values_arrays.append(dict_for_this_turn)

    # set starting task arrays:

    #################################
    # Setting start_project_array!!!
    #################################
    print("generating new start_project_array 2nd sweep")
    print(f"""
    starting_arraylength_n,       -> {starting_arraylength_n} {type(starting_arraylength_n)} 
    decimal_digits=0,             -> {decimal_digits} {type(decimal_digits)} 
    allow_negative_numbers=False, -> {allow_negative_numbers} {type(allow_negative_numbers)} 
    power_of_ten_scale=1          -> {power_of_ten_scale} {type(power_of_ten_scale)} 
    """)
    start_project_array = generate_random_starting_array(starting_arraylength_n, decimal_digits, allow_negative_numbers, power_of_ten_scale)
    print(f"start_project_array -> {start_project_array} {type(start_project_array)}")

    per_task_to_do__workspaces_values_arrays[0]["start_project_array"] = start_project_array.copy()

    print("created per_task_to_do__workspaces_values_arrays")
    print("per_task_to_do__workspaces_values_arrays ->")
    pp_list(per_task_to_do__workspaces_values_arrays)




    ######################################
    # loops here through unit-test making?
    ######################################

    for key, value in schedule_tree_dict.items():
        """
        iterate through the partially completed project-task-schedule
        - fill in:  operation_source_index_or_slice
        - fill in:  operation_sink_index_insert
        - fill in:  complete_natural_language_project_outline
        - fill out: unit tests

        create mis-steps and comments for effects of mis-steps

        In order to fill in the operation_source_index_or_slice,
        look at the per_task_to_do__workspaces_values_arrays[turn_counter][task_source]

        e.g.
        skeleton_schedule
        {1: {'role': 'Alice',
            'task_type': 'two_indices_type_operation',
            'task_source': 'start_project_array',
            'operation_source_index_or_slice': None,
            'task_sink': 'Bob',
            'operation_sink_index_insert': None,
            'task_blurb': 'perform subtraction on',
            'specific_task_operation': 'subtraction'},

        2: {'role': 'Bob',
            'task_type': 'one_slice_type_operation',
            'task_source': 'start_project_array',
            'operation_source_index_or_slice': None,
            'task_sink': 'start_project_array',
            'operation_sink_index_insert': None,
            'task_blurb': 'perform reverse on',
            'specific_task_operation': 'reverse'},

        """
        print(f"\n\niterating >> for key, value in schedule_tree_dict.items():")

        print("per_task_to_do__workspaces_values_arrays ->")
        pp_list(per_task_to_do__workspaces_values_arrays)

        # counting from one
        this_turn = key

        # index for this turn, offset counting from zero
        this_turn_index = key - 1

        # index of the turn ahead, after this turn
        next_turns_state_index = this_turn_index + 1

        print(f"key             -> {key}")
        print(f"this_turn       -> {this_turn}")
        print(f"this_turn_index -> {this_turn_index}")

        # print(f"per_task_to_do__workspaces_values_arrays")
        # print(per_task_to_do__workspaces_values_arrays)

        # prettyprint the list of dicts
        print(f"per_task_to_do__workspaces_values_arrays[key]")
        print(f"per_task_to_do__workspaces_values_arrays[{this_turn_index}] -> ")
        print(per_task_to_do__workspaces_values_arrays[this_turn_index])

        if key > 1:
            print("\nReview: the previous schedule tree task:")
            print(f"turn/key -> {key}")
            print("schedule_tree_dict[key - 1]")
            pprint(schedule_tree_dict[key - 1])
            print(f"\n\n")


        #######################
        # Set workplace source
        #######################
        print(f"Set workplace source")

        # In order to fill in the operation_source_index_or_slice
        task_source = value['task_source']
        print(f"task_source -> {task_source}")

        """
        off-by-one
        remember to -1 the turn/key (counts from 1),
        to make it equal the index (counts from zero) of lists
        """
        source_workspace = per_task_to_do__workspaces_values_arrays[this_turn_index][task_source].copy()

        # pick random location(s) in workspace
        print(f"get source_workspace -> {source_workspace}")

        source_workspace_copy = source_workspace.copy()

        task_type = value['task_type']
        specific_task_operation = value['specific_task_operation']

        print(f"task_type               -> {task_type}")
        print(f"specific_task_operation -> {specific_task_operation}")
        print(f"source_workspace_copy   -> {source_workspace_copy}")



        ##########################
        # next turn's proto-state
        ##########################
        """
        Set up the next turn's proto-state,
        the same as this turns starting 'current state'
        """
        if this_turn_index < (len(per_task_to_do__workspaces_values_arrays) - 1):
            copy_forward_initial_values__workspace_updater(
                per_task_to_do__workspaces_values_arrays,
                the_index_to_copy_forward=this_turn_index )

        else:
            print("last index, not next turn to set")




        ######################################
        # Set operation_source_index_or_slice
        ######################################
        """
        TODO:
        see how operation_source_index_or_slice is set in 
        two sections of code.
        - overwritten?
        - recorded correctly?
        - how to clean up version 2?

        set source index or slice
        set value, and set value in skeleton dict, not: None

        todo:
        make a separate value finder function...
        """

        ##########################
        # set index/slice/indices
        #  &
        # Set Values
        ##########################
        if task_type == 'one_slice_type_operation':

            # set operation_source_index_or_slice
            operation_source_index_or_slice = array_slice_finder_index_maker(source_workspace)

            # set the_slice_or_index_values
            the_slice_or_index_values = array_slice_value_finder(source_workspace, operation_source_index_or_slice)


        elif task_type == 'two_indices_type_operation':

             # set operation_source_index_or_slice
            operation_source_index_or_slice = array_two_index_finder_index_maker(source_workspace)

            # set the_slice_or_index_values
            the_slice_or_index_values = array_two_value_finder(source_workspace, operation_source_index_or_slice)


        elif task_type == 'one_index_type_operation':

            # set operation_source_index_or_slice
            operation_source_index_or_slice =  valid_single_index_finder_index_maker(source_workspace)

            # set the_slice_or_index_values
            the_slice_or_index_values = one_array_single_value_finder(source_workspace, operation_source_index_or_slice)

        else:
            print(f"Waaaaaaaaaaaaaaaaaaaaahhh HHHHHHHHHHHHHHHHuh??? {task_type}")
            sys.exit()


        # inspection
        print("Setting: operation_source_index_or_slice")
        print(f"source_workspace                -> {source_workspace}")
        print(f"task_type                       -> {task_type}")
        print(f"operation_source_index_or_slice -> {operation_source_index_or_slice}")
        print(f"the_slice_or_index_values       -> {the_slice_or_index_values}")

        # for this section set this AFTER, for next section lookup FIRST
        schedule_tree_dict[this_turn]['operation_source_index_or_slice'] = operation_source_index_or_slice
        # schedule_tree_dict[this_turn]['the_slice_or_index_values'] = the_slice_or_index_values




        #####################
        # Set workplace sink
        #####################
        print("setting sink index")
        task_sink = value['task_sink']

        sink_workspace = per_task_to_do__workspaces_values_arrays[this_turn_index][task_sink].copy()

        if sink_workspace:
            # pick random index inside...
            sink_index = random.randint(0, len(sink_workspace) - 1)


        else:

            sink_index = 0
            # operation_sink_index_insert

        print(f"sink_index     -> {sink_index}")
        print(f"sink_workspace -> {sink_workspace}")
        schedule_tree_dict[key]['operation_sink_index_insert'] = sink_index



        ##########################
        # carry out the operation
        ##########################
        """
        The indices/slice has to be decided on and recorded
        the operation must be carried out

        task_type
        1. two_indices_type_operation
        2. one_index_type_operation
        3. one_slice_type_operation

        specific_task_operation


        TODO:
        either above or below, redundant / overwriting?
        Which is recorded in skelington?

        """

        # operation
        if task_type == 'two_indices_type_operation':
            print("two_indices_type_operation")
            print(f"operation_source_index_or_slice  -> {operation_source_index_or_slice} {type(operation_source_index_or_slice)}")
            print(f"the_slice_or_index_values        -> {the_slice_or_index_values} {type(the_slice_or_index_values)}")

            index1 = operation_source_index_or_slice[0]
            index2 = operation_source_index_or_slice[1]
            print(f"index1 -> {index1} {type(index1)}")
            print(f"index2 -> {index2} {type(index2)}")
            operation_result = process_and_append_two_indices_operation(source_workspace_copy, index1, index2, specific_task_operation)

            ##############
            # Save Result  (to next turn's state)
            ##############
            per_task_to_do__workspaces_values_arrays[next_turns_state_index][task_sink].insert(sink_index, operation_result)


        elif task_type == 'one_index_type_operation':
            print("one_index_type_operation")
            print(f"operation_source_index_or_slice  -> {operation_source_index_or_slice} {type(operation_source_index_or_slice)}")
            print(f"the_slice_or_index_values        -> {the_slice_or_index_values} {type(the_slice_or_index_values)}")
            # TODO source operation_source_index_or_slice here
            operation_result = process_single_index_operation(source_workspace_copy, operation_source_index_or_slice, specific_task_operation)

            ##############
            # Save Result  (to next turn's state)
            ##############
            per_task_to_do__workspaces_values_arrays[next_turns_state_index][task_sink].insert(sink_index, operation_result)


        elif task_type == 'one_slice_type_operation':
            print("one_slice_type_operation")
            print(f"operation_source_index_or_slice  -> {operation_source_index_or_slice} {type(operation_source_index_or_slice)}")
            print(f"the_slice_or_index_values        -> {the_slice_or_index_values} {type(the_slice_or_index_values)}")
            operation_result = array_slice_operation_executor(specific_task_operation, operation_source_index_or_slice, source_workspace_copy)

            ##############
            # Save Result  (to next turn's state)
            ##############
            print(f"one_slice_type_operation, operation_result -> {operation_result}")

            if isinstance(operation_result, list):
                print("is list")

                # read results backward and feed in that way
                for this_item in operation_result[::-1]:
                    per_task_to_do__workspaces_values_arrays[next_turns_state_index][task_sink].insert(sink_index, this_item)

            else:  # not a list
                print("is NOT list")
                per_task_to_do__workspaces_values_arrays[next_turns_state_index][task_sink].insert(sink_index, operation_result)

        else:
            print("Waaaaaaaaa AAHHHHH!!!!!")


    print(f"""


    End of operation process summary:

    key, this turn  -> {key}
    value           -> {value}

    task_source     -> {task_source}
    source_workspace-> {source_workspace}

    task_sink       -> {task_sink}
    sink_index      -> {sink_index}
    sink_workspace  -> {sink_workspace}

    operation_result-> {operation_result}
    """)
    print("per_task_to_do__workspaces_values_arrays")
    pprint(per_task_to_do__workspaces_values_arrays)

    # print(complete_natural_language_project_outline)


    ######################
    # make unit_test data
    ######################
    starting_starting_array = per_task_to_do__workspaces_values_arrays[0]['start_project_array'].copy()
    final_end_result_project_array = per_task_to_do__workspaces_values_arrays[-1]['end_result_project_array'].copy()

    input_value = starting_starting_array.copy()
    ouput_value = final_end_result_project_array.copy()

    unit_test_dict = {"input": input_value, "expected_output": ouput_value}

    # collect unit test tuple
    test_cases_list.append(unit_test_dict)


    """
    output the random seed for repeatability

    output:

    output_tuple = (
        problem body json,
        skeleton,
        random seed,
    )


    """
    



    print("\n\nEnd of phase 2, schedule_tree_dict ->")
    pprint(schedule_tree_dict)

    """
    # todo: add n_unit_tests_to_make input parameter
    # Maybe a loop here for n_unit_tests_to_make
    for _ in range(n_unit_tests_to_make):
        # etc
    """
    print("\n\n\nMaking Unit Tests\n\n\n")

    unit_test_making_counter = 0

    for _ in range(n_unit_tests_to_make - 1):

        unit_test_making_counter += 1

        """
        Change the input array:
        - 
        - 
        - 
        - 
        """

        # 3rd sweep(s)
        print(f"\n\n\nMaking Unit Tests: unit_test_making_counter -> {unit_test_making_counter}\n\n\n")
        """
        - add operation_source_index_or_slice
        - perform operation
        - make unit tests
        -
        """

        """
        per_task_to_do__workspaces_values_arrays

        array of turn's taken or tasks done:
        each task-to-do-array is a dict:
        to lookup the workspace[array] for each workspace

        so for each task, there will be a set of all workspaces available
        for that task to act upon, in current state.


        TODO:
        Results:
        updates values are written to the next turn's
        'current' state
        unchanged values are copied as they are
        results update changed workspaces
        """

        per_task_to_do__workspaces_values_arrays = []

        # iterate through each task by each participant/role
        # add one more for the final result
        # for _ in range (len(turn_data_list) + 1):
        #     dict_for_this_turn = {}

        #     for this_workspace in all_array_workspace_list:
        #         dict_for_this_turn[this_workspace] = []

        #     # add that dict or workspaces for this task-to-do
        #     import copy
        #     superfluous_copy_of_dict = copy.deepcopy(dict_for_this_turn)
        #     per_task_to_do__workspaces_values_arrays.append(superfluous_copy_of_dict)

        # iterate through each task by each participant/role
        # add one more for the final result
        for _ in range (len(turn_data_list) + 1):
            dict_for_this_turn = {this_workspace: [] for this_workspace in all_array_workspace_list}
            per_task_to_do__workspaces_values_arrays.append(dict_for_this_turn)

        # set starting task arrays:

        #################################
        # Setting start_project_array!!!
        #################################

        print(f"generating new start_project_array, unit_test_making_counter -> {unit_test_making_counter}")
        print(f"""
        starting_arraylength_n,       -> {starting_arraylength_n} {type(starting_arraylength_n)} 
        decimal_digits=0,             -> {decimal_digits} {type(decimal_digits)} 
        allow_negative_numbers=False, -> {allow_negative_numbers} {type(allow_negative_numbers)} 
        power_of_ten_scale=1          -> {power_of_ten_scale} {type(power_of_ten_scale)} 
        """)

        start_project_array = generate_random_starting_array(starting_arraylength_n, decimal_digits, allow_negative_numbers, power_of_ten_scale)

        print(f"start_project_array -> {start_project_array} {type(start_project_array)}")

        per_task_to_do__workspaces_values_arrays[0]["start_project_array"] = start_project_array.copy()

        print("created per_task_to_do__workspaces_values_arrays")
        print("per_task_to_do__workspaces_values_arrays ->")
        pp_list(per_task_to_do__workspaces_values_arrays)




        ######################################
        # loops here through unit-test making?
        ######################################

        for key, value in schedule_tree_dict.items():
            """
            iterate through the partially completed project-task-schedule
            - fill in:  operation_source_index_or_slice
            - fill in:  operation_sink_index_insert
            - fill in:  complete_natural_language_project_outline
            - fill out: unit tests

            create mis-steps and comments for effects of mis-steps

            In order to fill in the operation_source_index_or_slice,
            look at the per_task_to_do__workspaces_values_arrays[turn_counter][task_source]

            e.g.
            skeleton_schedule
            {1: {'role': 'Alice',
                'task_type': 'two_indices_type_operation',
                'task_source': 'start_project_array',
                'operation_source_index_or_slice': None,
                'task_sink': 'Bob',
                'operation_sink_index_insert': None,
                'task_blurb': 'perform subtraction on',
                'specific_task_operation': 'subtraction'},

            2: {'role': 'Bob',
                'task_type': 'one_slice_type_operation',
                'task_source': 'start_project_array',
                'operation_source_index_or_slice': None,
                'task_sink': 'start_project_array',
                'operation_sink_index_insert': None,
                'task_blurb': 'perform reverse on',
                'specific_task_operation': 'reverse'},

            """

            # clean
            role = None 
            task_type = None 
            task_source = None 
            operation_source_index_or_slice = None 
            task_sink = None 
            operation_sink_index_insert = None 
            task_blurb = None 
            specific_task_operation = None 

            print(f"\n\niterating >> for key, value in schedule_tree_dict.items():")

            print("per_task_to_do__workspaces_values_arrays ->")
            pp_list(per_task_to_do__workspaces_values_arrays)

            # counting from one
            this_turn = key

            # index for this turn, offset counting from zero
            this_turn_index = key - 1

            # index of the turn ahead, after this turn
            next_turns_state_index = this_turn_index + 1

            print(f"key             -> {key}")
            print(f"this_turn       -> {this_turn}")
            print(f"this_turn_index -> {this_turn_index}")

            # print(f"per_task_to_do__workspaces_values_arrays")
            # print(per_task_to_do__workspaces_values_arrays)

            # prettyprint the list of dicts
            print(f"\n per_task_to_do__workspaces_values_arrays[key]")
            print(f"per_task_to_do__workspaces_values_arrays[{this_turn_index}] -> ")
            print(per_task_to_do__workspaces_values_arrays[this_turn_index])

            if key > 1:
                print("\nReview: the previous schedule tree task:")
                print(f"turn/key -> {key}")
                print("schedule_tree_dict[key - 1]")
                pprint(schedule_tree_dict[key - 1])
                print(f"\n\n")

            #############################################
            # Retrieving values from skeleton dictionary
            #############################################
            print(f"Retrieving values from skeleton dictionary")

            # In order to fill in the operation_source_index_or_slice
            role = value['role']
            task_type = value['task_type']
            task_source = value['task_source']
            operation_source_index_or_slice = value['operation_source_index_or_slice']
            task_sink = value['task_sink']
            operation_sink_index_insert = value['operation_sink_index_insert']
            task_blurb = value['task_blurb']
            specific_task_operation = value['specific_task_operation']

            print(f"role                    -> {role}")
            print(f"task_type               -> {task_type}")
            print(f"task_source             -> {task_source}")
            print(f"operation_source_index_or_slice -> {operation_source_index_or_slice}")
            print(f"task_sink               -> {task_sink}")
            print(f"source_workspace_copy   -> {source_workspace_copy}")
            print(f"task_blurb              -> {task_blurb}")
            print(f"specific_task_operation -> {specific_task_operation}\n\n")

            """
            off-by-one
            remember to -1 the turn/key (counts from 1),
            to make it equal the index (counts from zero) of lists
            """
            source_workspace = per_task_to_do__workspaces_values_arrays[this_turn_index][task_source].copy()

            # pick random location(s) in workspace
            print(f"source_workspace -> {source_workspace}")

            source_workspace_copy = source_workspace.copy()






            ##########################
            # next turn's proto-state
            ##########################
            """
            Set up the next turn's proto-state,
            the same as this turns starting 'current state'
            """
            print("setting next turn's proto-state (s) ")
            if this_turn_index < (len(per_task_to_do__workspaces_values_arrays) - 1):
                copy_forward_initial_values__workspace_updater(
                    per_task_to_do__workspaces_values_arrays,
                    the_index_to_copy_forward=this_turn_index )

            else:
                print("last index, not next turn to set")



            # # inspection
            print("Retrieving: operation_source_index_or_slice")
            print(f"source_workspace                -> {source_workspace}")
            print(f"task_type                       -> {task_type}")


            #############
            # Set Values
            #############
            if task_type == 'one_slice_type_operation':

                # set the_slice_or_index_values
                the_slice_or_index_values = array_slice_value_finder(source_workspace, operation_source_index_or_slice)

            elif task_type == 'two_indices_type_operation':

                # set the_slice_or_index_values
                the_slice_or_index_values = array_two_value_finder(source_workspace, operation_source_index_or_slice)

            elif task_type == 'one_index_type_operation':

                # set the_slice_or_index_values
                the_slice_or_index_values = one_array_single_value_finder(source_workspace, operation_source_index_or_slice)

            else:
                print("Waaaaaaaaaaaaaaaaaaaaahhh HHHHHHHHHHHHHHHHuh???")
                sys.exit()

            # inspection
            print("Retrieving: operation_source_index_or_slice")
            print(f"task_type                       -> {task_type}")
            print(f"source_workspace                -> {source_workspace}")
            print(f"operation_source_index_or_slice -> {operation_source_index_or_slice}")
            print(f"the_slice_or_index_values       -> {the_slice_or_index_values}")


            """
            todo:
            getting sink and source slice/indices
            """

            #####################
            # Set workplace sink
            #####################
            print("retrieving sink index")
            sink_index = schedule_tree_dict[key]['operation_sink_index_insert']
            print(f"sink_index -> {sink_index}")

            print("retrieving task_sink")
            task_sink = value['task_sink']
            print(f"task_sink -> {task_sink}")

            sink_workspace = per_task_to_do__workspaces_values_arrays[this_turn_index][task_sink].copy()
            print(f"sink_workspace -> {sink_workspace}")


            ##########################
            # carry out the operation
            ##########################
            """
            The indices/slice has to be decided on and recorded
            the operation must be carried out

            task_type
            1. two_indices_type_operation
            2. one_index_type_operation
            3. one_slice_type_operation

            specific_task_operation


            TODO:
            either above or below, redundant / overwriting?
            Which is recorded in skelington?

            """
            print("\n\ncarry out the operation")

            # operation
            if task_type == 'two_indices_type_operation':
                print("two_indices_type_operation")
                print(f"operation_source_index_or_slice  -> {operation_source_index_or_slice} {type(operation_source_index_or_slice)}")
                print(f"the_slice_or_index_values        -> {the_slice_or_index_values} {type(the_slice_or_index_values)}")

                index1 = operation_source_index_or_slice[0]
                index2 = operation_source_index_or_slice[1]
                print(f"index1 -> {index1} {type(index1)}")
                print(f"index2 -> {index2} {type(index2)}")
                operation_result = process_and_append_two_indices_operation(source_workspace_copy, index1, index2, specific_task_operation)

                ##############
                # Save Result  (to next turn's state)
                ##############
                print(f"two_indices_type_operation, operation_result -> {operation_result}")
                per_task_to_do__workspaces_values_arrays[next_turns_state_index][task_sink].insert(sink_index, operation_result)
                print(f"per_task_to_do__workspaces_values_arrays[next_turns_state_index] -> {per_task_to_do__workspaces_values_arrays[next_turns_state_index]}")


            elif task_type == 'one_index_type_operation':
                print("one_index_type_operation")
                print(f"operation_source_index_or_slice  -> {operation_source_index_or_slice} {type(operation_source_index_or_slice)}")
                print(f"the_slice_or_index_values        -> {the_slice_or_index_values} {type(the_slice_or_index_values)}")
                # TODO source operation_source_index_or_slice here
                operation_result = process_single_index_operation(source_workspace_copy, operation_source_index_or_slice, specific_task_operation)

                ##############
                # Save Result  (to next turn's state)
                ##############
                print(f"one_index_type_operation, operation_result -> {operation_result}")
                per_task_to_do__workspaces_values_arrays[next_turns_state_index][task_sink].insert(sink_index, operation_result)
                print(f"per_task_to_do__workspaces_values_arrays[next_turns_state_index] -> {per_task_to_do__workspaces_values_arrays[next_turns_state_index]}")


            elif task_type == 'one_slice_type_operation':
                print("one_slice_type_operation")
                print(f"operation_source_index_or_slice  -> {operation_source_index_or_slice} {type(operation_source_index_or_slice)}")
                print(f"the_slice_or_index_values        -> {the_slice_or_index_values} {type(the_slice_or_index_values)}")
                operation_result = array_slice_operation_executor(specific_task_operation, operation_source_index_or_slice, source_workspace_copy)

                ##############
                # Save Result  (to next turn's state)
                ##############
                print(f"one_slice_type_operation, operation_result -> {operation_result}")

                if isinstance(operation_result, list):
                    print("is list")

                    # read results backward and feed in that way
                    for this_item in operation_result[::-1]:
                        per_task_to_do__workspaces_values_arrays[next_turns_state_index][task_sink].insert(sink_index, this_item)
                        print(f"per_task_to_do__workspaces_values_arrays[next_turns_state_index] -> {per_task_to_do__workspaces_values_arrays[next_turns_state_index]}")

                else:  # not a list
                    print("is NOT list")
                    per_task_to_do__workspaces_values_arrays[next_turns_state_index][task_sink].insert(sink_index, operation_result)
                    print(f"per_task_to_do__workspaces_values_arrays[next_turns_state_index] -> {per_task_to_do__workspaces_values_arrays[next_turns_state_index]}")

            else:
                print("Waaaaaaaaa AAHHHHH!!!!!")





            print(f"""


            End of this unit-test making operation process summary:

            key, this turn  -> {key}
            value           -> {value}

            task_source     -> {task_source}
            source_workspace-> {source_workspace}

            task_sink       -> {task_sink}
            sink_index      -> {sink_index}
            sink_workspace  -> {sink_workspace}

            operation_result-> {operation_result}
            """)
            print("per_task_to_do__workspaces_values_arrays")
            pprint(per_task_to_do__workspaces_values_arrays)

            print(complete_natural_language_project_outline)


        ######################
        # make unit_test data
        ######################


        # starting_starting_array = 

        starting_starting_array = per_task_to_do__workspaces_values_arrays[0]['start_project_array'].copy()
        final_end_result_project_array = per_task_to_do__workspaces_values_arrays[-1]['end_result_project_array'].copy()

        input_value = starting_starting_array.copy()
        ouput_value = final_end_result_project_array.copy()

        unit_test_dict = {"input": input_value, "expected_output": ouput_value}

        # collect unit test tuple
        test_cases_list.append(unit_test_dict)

        print(f"""
        make unit_test data:

        unit_test_dict  -> {unit_test_dict}
                
        """)

    """
    Todo:
    loop to make N unit-tests

    output json for problem-maker...

    output problem-maker script


    overall blurb

    problem paragraph

    unit tests:
    - starting array
    - ending array


    Write one or more functions in {programming_language},
    where the input is any starting array,
    and the needed output is the final ending array
    after the following project schedule process.
    
    This is a sequential turn-based project where participants
    perform tasks changing values in arrays.
    Feeding into the final ending array of results,
    there is the starting array and each participant has workspace array. 
    There are {n} participants.
    Each participant has {n} tasks.
    This is the project operation schedule: 
    {problem_description_paragraph}.


    """
    ##################
    # make full blurb
    ##################
    """
    todo
    full puzzle description...is
    all the parts added together.
    """
    pprint(schedule_tree_dict)


    for key, value in schedule_tree_dict.items():
        blurb = describe_task(value)
        print(blurb)
        print("\n")

        complete_natural_language_project_outline += blurb


    test_cases = test_cases_list.copy()

    programming_language = "python"


    task = f"""Write one or more functions in the {programming_language} language, 
    with the main function called project_tasks_puzzle() 
    where the input is a starting array, 
    and the needed output is the final ending array 
    after the following project schedule process, 
    so, def project_tasks_puzzle([array]): is the main function 
    and the output is one array of values. 

    This is a sequential turn-based project where participants 
    perform tasks changing values in arrays. 
    Feeding into the final ending array of results 
    there is a starting array (the one input parameter) and 
    each participant has workspace array. 
    There are {r_number_of_roles} roles or participants. 
    Each participant has {t_number_of_turns} tasks. 
    This is the project operation schedule: 
    {complete_natural_language_project_outline}
    """

    ###############
    # Final Return
    ###############
    print("per_task_to_do__workspaces_values_arrays")
    pprint(per_task_to_do__workspaces_values_arrays)

    the_final_countdown = per_task_to_do__workspaces_values_arrays[-1]['end_result_project_array'].copy()
    print("the_final_countdown")
    pprint(the_final_countdown)

    print(f"""
    complete_natural_language_project_outline ->
    {complete_natural_language_project_outline}

    test_cases_list ->
    {test_cases_list}

    programming_language
    complete_natural_language_project_outline
    test_cases
    r_number_of_roles,
    t_number_of_turns,
    starting_arraylength_n,
    decimal_digits=decimal_digits,
    allow_negative_numbers=allow_negative_numbers,
    power_of_ten_scale=power_of_ten_scale,
    n_unit_tests_to_make=n_unit_tests_to_make

    """)



    json_body = create_json_body(programming_language, complete_natural_language_project_outline, test_cases, r_number_of_roles, t_number_of_turns)
    print(json_body)

    print("json_body")
    pprint(json_body)

    # main_question = ""
    # main_question += f"Write one or more functions in "
    # main_question += f"{programming_language}, "
    # main_question += "where the input is any starting array, "
    # main_question += "and the needed output is the final ending array "
    # main_question += "after the following project schedule process "
    # main_question += f"{problem_description_paragraph}."

    # problem_body_json = {
    #     'programming_language': programming_language,
    #     'main_question': main_question,
    #     'problem_description_paragraph': problem_description_paragraph,
    #     'test_cases':test_cases_list
    # }

    ###
    # 
    ###

    python_random_current_state = random.getstate()
    # print(python_random_current_state)

    test_set_name = "project_puzzle_code_writing_test_set_1.jsonl"

    with open(test_set_name, "a") as file:
        json_writedata = json.dumps(json_body)
        file.write(json_writedata + "\n")
    print("Challenge JSONL file created successfully.")


    import time

    # Get the current timestamp
    current_timestamp = time.time()

    # Convert the timestamp to a readable format
    local_time = time.localtime(current_timestamp)
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)

    # print(formatted_time)

    # Open a file in append mode
    with open(f"output_{formatted_time}.txt", "a") as file:
        # Write the values of the variables to the file, each on a new line
        file.write(f"schedule_tree_dict: {str(schedule_tree_dict)}\n")
        file.write(f"python_random_current_state: {str(python_random_current_state)}\n")
        file.write(f"json_body: {str(json_body)}\n")

        # Print a message for each variable written to the file
        print(f"The values have been written to the file 'output.txt'.")

    return json_body, python_random_current_state, schedule_tree_dict



"""
Append coding challenges to a test set
"""
test_set_name = "code_writing_test_set_8.jsonl"

import json

# # Optional
# from datetime import datetime, UTC
# date_time = datetime.now(UTC)
# clean_timestamp = date_time.strftime("%Y%m%d%H%M%S%f")   


# function to make jsonl for coding tests
def create_challenge_json(function_name, input_parameters, project_puzzle_and_output_description, test_cases, programming_language):

    task = f"""
    Write a function called {function_name}() in the {programming_language} language, 

    
    Write one or more functions in {programming_language}, 
    with the main function called {function_name}() 
    where the input is any starting array, 
    and the needed output is the final ending array 
    after the following project schedule process,
    such that input is ({', '.join(input_parameters)}), 
    so, def {function_name}({', '.join(input_parameters)}): 
    and the output is {project_puzzle_and_output_description} 
    
    This is a sequential turn-based project where participants 
    perform tasks changing values in arrays. 
    Feeding into the final ending array of results, 
    there is the starting array and each participant has workspace array.  
    There are {n} participants. 
    Each participant has {n} tasks. 
    This is the project operation schedule: 
    {problem_description_paragraph}. 
    """

    challenge_data = {
        "task": task,
        "function_name": function_name,
        "input_parameters": input_parameters,
        "project_puzzle_and_output_description": project_puzzle_and_output_description,
        "test_cases": test_cases,
        "programming_language": programming_language
    }


    with open(test_set_name, "a") as file:
        json_data = json.dumps(challenge_data)
        file.write(json_data + "\n")
    print("Challenge JSONL file created successfully.")


##################
# Make The Tests! 
##################


# calculate_right_triangle_area
function_name = "project_puzzle"
input = "one array of values"
input_parameters = ["array_of_values"]
project_puzzle_and_output_description = "Alice is going to perform bitwise_or on the 'bitwise_or' operation on the data from 'start_project_array' and store the result in 'start_project_array'. The operation will be performed on the elements at indices 3 and 1.Bob is going to perform bitwise_or on the 'bitwise_or' operation on the data from 'start_project_array' and store the result in 'start_project_array'. The operation will be performed on the elements at indices 2 and 1.Bob is going to perform sort on the 'sort' operation on the data from 'start_project_array' and store the result in 'end_result_project_array'. The operation will be performed on the slice from index 0 to (but not including) index 4.Alice is going to apply the bitwise NOT operation to the 'bitwise_not' operation on the data from 'end_result_project_array' and store the result in 'end_result_project_array'. The operation will be performed on the element at index 0."
test_cases = [
    {
        "input": [9, 2, 0, 8],
        "expected_output": [1, -1, 2]
    },
    {
        "input": [2, 3, 5, 8],
        "expected_output": [1, -1, 3]
    },
    {
        "input": [2, 2, 9, 9],
        "expected_output": [1, -1, 2]
    },
    {
        "input": [9, 7, 5, 6],
        "expected_output": [3, -7, 7]]
    },
    {
        "input": [6, 3, 9, 3],
        "expected_output": [1, -4, 3]
    },
    {
        "input": [2, 8, 9, 5],
        "expected_output": [4, -1, 8]
    },
]
programming_language = 'rust'
create_challenge_json(function_name, input_parameters, project_puzzle_and_output_description, test_cases, programming_language)


# calculate_right_triangle_area
function_name = "project_tasks_puzzle"
input = "one array of values"
input_parameters = ["array_of_values"]
complete_natural_language_project_outline = "Alice is going to perform bitwise_or on the 'bitwise_or' operation on the data from 'start_project_array' and store the result in 'start_project_array'. The operation will be performed on the elements at indices 3 and 1.Bob is going to perform bitwise_or on the 'bitwise_or' operation on the data from 'start_project_array' and store the result in 'start_project_array'. The operation will be performed on the elements at indices 2 and 1.Bob is going to perform sort on the 'sort' operation on the data from 'start_project_array' and store the result in 'end_result_project_array'. The operation will be performed on the slice from index 0 to (but not including) index 4.Alice is going to apply the bitwise NOT operation to the 'bitwise_not' operation on the data from 'end_result_project_array' and store the result in 'end_result_project_array'. The operation will be performed on the element at index 0."
test_cases = [
    {
        "input": [9, 2, 0, 8],
        "expected_output": [1, -1, 2]
    },
    {
        "input": [2, 3, 5, 8],
        "expected_output": [1, -1, 3]
    },
    {
        "input": [2, 2, 9, 9],
        "expected_output": [1, -1, 2]
    },
    {
        "input": [9, 7, 5, 6],
        "expected_output": [3, -7, 7]]
    },
    {
        "input": [6, 3, 9, 3],
        "expected_output": [1, -4, 3]
    },
    {
        "input": [2, 8, 9, 5],
        "expected_output": [4, -1, 8]
    },
]
programming_language = 'rust'
create_challenge_json(function_name, input_parameters, project_puzzle_and_output_description, test_cases, programming_language)




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
    
    
    
{task:"""
Write a function called project_tasks_puzzle() in the python language, 
Write one or more functions in the python language, 
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
There are 2 roles or participants. 
Each participant has 2 tasks. 
This is the project operation schedule: 
Bob is going to perform reverse on the data from 'start_project_array' and insert the result at index 0 in 'Bob' (inserting, not replacing any values). The 'reverse' operation will be performed on the slice from index 0 to (but not including) index 5.
Alice is going to apply the identity function to the data from 'Bob' and insert the result at index 0 in 'end_result_project_array' (inserting, not replacing any values). The 'identity' operation will be performed on the element at index 0.
Bob is going to perform sort on the data from 'start_project_array' and insert the result at index 0 in 'end_result_project_array' (inserting, not replacing any values). The 'sort' operation will be performed on the slice from index 1 to (but not including) index 3.
Alice is going to perform multiplication on the data from 'end_result_project_array' and insert the result at index 0 in 'end_result_project_array' (inserting, not replacing any values). The 'multiplication' operation will be performed on the elements at indices 0 and 1.
""",
    "function_name": "project_tasks_puzzle", 
    "input_parameters": ["one array of values"], 
    "output_description": "The final array of project results", 
    "test_cases": [{"input": [5, 3], "expected_output": 15.0}, {"input": [2.5, 4], "expected_output": 10.0}]}
    
    
    {"task": "\n    Write a python function called calculate_area(), \n    such that given input(s) are (length, width),\n    so, def calculate_area(length, width):\n    and the output is The area of a rectangle, only return a number \n    ", "function_name": "calculate_area", "input_parameters": ["length", "width"], "output_description": "The area of a rectangle, only return a number", "test_cases": [{"input": [5, 3], "expected_output": 15.0}, {"input": [2.5, 4], "expected_output": 10.0}]}
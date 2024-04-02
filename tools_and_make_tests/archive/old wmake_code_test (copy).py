
# code
import json

def create_challenge_json(function_name, input_parameters, output_description, test_cases):
    challenge_data = {
        "function_name": function_name,
        "input_parameters": input_parameters,
        "output_description": output_description,
        "test_cases": test_cases
    }

    with open("write_a_make_a_function_challenge.jsonl", "a") as file:
        json.dump(challenge_data, file, indent=4)

    print("Challenge JSON file created successfully.")

# Example usage
function_name = "calculate_area"
input_parameters = ["length", "width"]
output_description = "The area of a rectangle"
test_cases = [
    {
        "input": [5, 3],
        "expected_output": 15
    },
    {
        "input": [2.5, 4],
        "expected_output": 10
    }
]

create_challenge_json(function_name, input_parameters, output_description, test_cases)


import json

def create_challenge_json(function_name, input_parameters, output_description, test_cases):
    challenge_data = {
        "function_name": function_name,
        "input_parameters": input_parameters,
        "output_description": output_description,
        "test_cases": test_cases
    }
    with open("write_a_make_a_function_challenge.json", "a") as file:
        json_data = json.dumps(challenge_data)
        file.write(json_data + "\n")
    print("Challenge JSON file created successfully.")

# Example usage
function_name = "calculate_area"
input_parameters = ["length", "width"]
output_description = "The area of a rectangle"
test_cases = [
    {
        "input": [5, 3],
        "expected_output": 15
    },
    {
        "input": [2.5, 4],
        "expected_output": 10
    }
]
create_challenge_json(function_name, input_parameters, output_description, test_cases)


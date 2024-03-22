import json


def multiple_choice_append_to_jsonl(file_path, task, options, answer_index_from_1):
    data = {
        "task": task,
        "options": options,
        "answer_from_index": answer_index_from_1,
    }

    with open(file_path, "a", encoding="utf-8") as file:
        json.dump(data, file)
        file.write("\n")


def open_question_append_to_jsonl(file_path, task, options, answer):
    data = {
        "task": task,
        "options": options,
        "answer": answer,
    }

    with open(file_path, "a", encoding="utf-8") as file:
        json.dump(data, file)
        file.write("\n")

task_file_directory = "ai_task_files"

########################
# Multiple Choice Tests
########################
# multiple_choice_append_to_jsonl(
#     f"{task_file_directory}/my_multiple_choice_test_1.jsonl", "What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "1")

# multiple_choice_append_to_jsonl(
#     f"{task_file_directory}/my_multiple_choice_test_1.jsonl", "What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars", "Venus"], "2")


multiple_choice_append_to_jsonl(
    f"{task_file_directory}/animal_multiple_choice_test_1.jsonl", "Is a cat an animal?", ["yes", "no"], "1")

multiple_choice_append_to_jsonl(
    f"{task_file_directory}/animal_multiple_choice_test_1.jsonl", "Is a dog an animal?", ["yes", "no"], "1")

multiple_choice_append_to_jsonl(
    f"{task_file_directory}/animal_multiple_choice_test_1.jsonl", "Is a human an animal?", ["yes", "no"], "1")

multiple_choice_append_to_jsonl(
    f"{task_file_directory}/animal_multiple_choice_test_1.jsonl", "Is a rock an animal?", ["yes", "no"], "2")

multiple_choice_append_to_jsonl(
    f"{task_file_directory}/animal_multiple_choice_test_1.jsonl", "Is a planet an animal?", ["yes", "no"], "2")

multiple_choice_append_to_jsonl(
    f"{task_file_directory}/animal_multiple_choice_test_1.jsonl", "Is a void an animal?", ["yes", "no"], "2")

####################
# Open Answer Tests
####################

"""
mark answers with numbers
answer A is 1
answer b is 2
"""
# "question", ["list","of","answers"], "answer_index_from_1"
# "The city councilmen refused the demonstrators a permit because they feared violence.", ["1. The city councilmen", "2. The demonstrators"], "1"



####################
# Open Answer Tests
####################
open_question_append_to_jsonl(f"{task_file_directory}/my_open_answer_test_1.jsonl", "What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars", "Venus"], "Jupiter")

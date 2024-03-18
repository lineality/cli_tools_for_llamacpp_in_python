import json


def multiple_choice_append_to_jsonl(file_path, task, options):
    data = {
        "task": task,
        "options": options,
        "answer": answer,
        "answer_from_index": answer_index_from,
    }

    with open(file_path, "a", encoding="utf-8") as file:
        json.dump(data, file)
        file.write("\n")


def open_question_append_to_jsonl(file_path, task, options):
    data = {
        "task": task,
        "options": options,
        "answer": answer,
        "answer_from_index": answer_index_from,
    }

    with open(file_path, "a", encoding="utf-8") as file:
        json.dump(data, file)
        file.write("\n")


########################
# Multiple Choice Tests
########################
multiple_choice_append_to_jsonl("my_multiple_choice_test_1.jsonl", "What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "1")
multiple_choice_append_to_jsonl("my_multiple_choice_test_1.jsonl", "What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars", "Venus"], "2")


####################
# Open Answer Tests
####################
open_question_append_to_jsonl("my_open_answer_test_1.jsonl", "What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars", "Venus"], "Jupiter")

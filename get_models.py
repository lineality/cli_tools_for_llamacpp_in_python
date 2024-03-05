from module_llamacpp import get_model_path_by_name
import os

"""
e.g.
'model_path_base': "/home/oops/jan/models/",
'model_nickname': f{use_this_model},
# /home/oops/jan/models/mistral-ins-7b-q4/mistral-7b-instruct-v0.2.Q4_K_M.gguf
"""


def get_absolute_base_path():
    # Get the absolute path to the current user's home directory (Starts from root, ends at home directory)
    home_directory = os.path.expanduser("~")  # e.g., "/home/john"

    absolute_path = os.path.abspath(home_directory)

    return absolute_path


def add_segment_to_absolute_base_path(additional_segment):
    # Get the absolute path to the current user's home directory
    home_directory = os.path.expanduser("~")
    # print(f"Home Directory: {home_directory}")  # Debugging print

    # Create an absolute path by joining the home directory with the additional segment
    absolute_path = os.path.join(home_directory, additional_segment)
    # print(f"Joined Path Before abspath: {absolute_path}")  # Debugging print

    # Ensure the path is absolute (this should not change the path if already absolute)
    absolute_path = os.path.abspath(absolute_path)
    # print(f"Final Absolute Path: {absolute_path}")  # Debugging print

    return absolute_path


model_name = input("Model name is...")

model_path_base = add_segment_to_absolute_base_path("jan/models/")

result = get_model_path_by_name(model_path_base, model_name)

print(result)

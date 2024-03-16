
import os
from datetime import datetime, UTC

def make_answers_directory_and_csv_path(this_original_task_file, model_name):
    """
    Returns a list of .json files in the current working directory.
    """
    solution_dir_path = "solution_files"
    date_time = datetime.now(UTC)
    clean_timestamp = date_time.strftime("%Y%m%d%H%M%S%f")


    # make path absolute
    solution_dir_path = os.path.abspath(solution_dir_path)

    # Check if the directory exists
    if not os.path.exists(solution_dir_path):

        # If it does not exist, create it
        # Ensure the directory exists
        try:
            os.makedirs(
                solution_dir_path, exist_ok=True
            )  # Ensure the directory is created if it does not exist
        except Exception as e:
            print(f"Error creating directory {solution_dir_path}: {e}")
            return  # Exit the function if directory creation fails



    # make path absolute, belts and suspenders
    solution_dir_path = os.path.abspath(solution_dir_path)

    # Extract just the last part of {model_name} and {this_original_task_file}
    model_name_last_part = os.path.basename(model_name).replace('.', '_')  # Replacing dots to avoid file extension confusion
    original_task_file_last_part = os.path.basename(this_original_task_file).replace('.', '_')

    answer_file_path = f"answer_file_{model_name_last_part}_{clean_timestamp}_{original_task_file_last_part}.csv" 

    # Determine the path to the file that should be saved
    answer_file_path = os.path.join(solution_dir_path, answer_file_path)

    # TODO: 
    # 1. extract just the last part of {model_name}
    # 2. extract just the last part of {this_original_task_file}
    # 3. make path, create directories and empty file


    # Create directories if they don't exist
    os.makedirs(os.path.dirname(answer_file_path), exist_ok=True)

    header_string = '"score", "this_row_or_line", "best_key_option", "use_this_model", "this_original_task_file", "task_from_instructions", "question_task_prompt", "list_of_options", "draft_task_attempt_log", "readable_timestamp"\n'

    # Create an empty file (or just close it if it already exists)
    with open(answer_file_path, 'a', newline='') as csvfile:
        csvfile.write(header_string)

    return answer_file_path


make_answers_directory_and_csv_path("abc", "xyz")
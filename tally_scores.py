import os
import csv

def score_tally(directory_path):
    
    # make path absolute
    solution_dir_path = os.path.abspath("solution_files")

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

    header_string = '"percent", "model", "score"\n' 

    # Create an empty file (or just close it if it already exists)
    with open("solution_files/score_report.csv", 'a', newline='') as csvfile:
        csvfile.write(header_string)


    
    
    
    model_scores = {}
    total_scores = 0
    # Iterating through files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory_path, filename)
            print(f"Processing file: {file_path}")  # Keep this print statement
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                print("reading...")  # Keep this print statement
                for row in reader:
                    model_name = row.get('use_this_model', 'Unknown')
                    print(model_name)  # Keep this print statement for model_name
                    score = int(row.get('score', 0))
                    # Update the scores and counts for each model
                    if model_name not in model_scores:
                        model_scores[model_name] = {'total': 0, 'count': 0}
                    
                    model_scores[model_name]['total'] += score
                    model_scores[model_name]['count'] += 1
                    total_scores += score
    # Preparing and printing the report
    report_list = []
    for model_name, score_data in model_scores.items():
        percentage = (score_data['total'] / total_scores) * 100 if total_scores > 0 else 0
        report_line = f'"{percentage:.0f}%", "{model_name}", "score {score_data['total']} / {score_data['count']}"\n'
        report_list.append(report_line)
        print(report_line)  # Print each line of the report
    # Joining the report lines and writing to a file
    for this_report_str in report_list:
        with open(os.path.join(directory_path, "score_report.csv"), 'a') as report_file:
            report_file.write(this_report_str)
            print(f"Report saved to {os.path.join(directory_path, 'score_report.txt')}")  # Confirmation message

score_tally("solution_files")


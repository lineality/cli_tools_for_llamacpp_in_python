import os
import csv

# def score_tally(directory_path):
#     model_scores = {}
#     total_scores = 0

#     for filename in os.listdir(directory_path):
#         if filename.endswith(".csv"):
#             file_path = os.path.join(directory_path, filename)

#             print(file_path)
#             with open(file_path, 'r') as file:
#                 reader = csv.DictReader(file)
#                 print("reading...")
#                 for row in reader:
#                     model_name = row['use_this_model']
#                     print(model_name)
#                     score = int(row['score'])

#                     if model_name in model_scores:
#                         model_scores[model_name]['total'] += score
#                         model_scores[model_name]['count'] += 1
#                     else:
#                         model_scores[model_name] = {'total': score, 'count': 1}

#                     total_scores += score

#     report = []
#     for model_name, score_data in model_scores.items():
#         percentage = (score_data['total'] / total_scores) * 100
#         report.append(f"{percentage:.0f}%: {model_name} score {score_data['total']} / {score_data['count']}")

#     report_str = '\n'.join(report)
#     print(report_str)

#     with open(os.path.join(directory_path, 'score_report.txt'), 'w') as report_file:
#         report_file.write(report_str)

import os
import csv

def score_tally(directory_path):
    model_scores = {}
    total_scores = 0

    # Iterating through files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory_path, filename)
            print(f"Processing file: {file_path}") # Keep this print statement

            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                print("reading...") # Keep this print statement
                for row in reader:
                    model_name = row['use_this_model']
                    print(model_name) # Keep this print statement for model_name
                    score = int(row['score'])

                    # Update the scores and counts for each model
                    if model_name not in model_scores:
                        model_scores[model_name] = {'total': 0, 'count': 0}
                    
                    model_scores[model_name]['total'] += score
                    model_scores[model_name]['count'] += 1
                    total_scores += score

    # Preparing and printing the report
    report = []
    for model_name, score_data in model_scores.items():
        percentage = (score_data['total'] / total_scores) * 100
        report_line = f"{percentage:.0f}%: {model_name} score {score_data['total']} / {score_data['count']}"
        report.append(report_line)
        print(report_line) # Print each line of the report

    # Joining the report lines and writing to a file
    report_str = '\n'.join(report)
    with open(os.path.join(directory_path, 'score_report.txt'), 'w') as report_file:
        report_file.write(report_str)
        print(f"Report saved to {os.path.join(directory_path, 'score_report.txt')}") # Confirmation message

# Example usage
# score_tally("solution_files")


score_tally("solution_files")
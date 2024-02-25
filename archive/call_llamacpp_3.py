# gpt4 OpenAI
import subprocess

# Define the command as a string
command = """
make -j && ./main 2>/dev/null -m /home/oops/jan/models/tinyllama-1.1b/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf -p "What is a horseshoe crab?"
"""

# Define the command as a string
command = """
./main 2>/dev/null -m /home/oops/jan/models/tinyllama-1.1b/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf -p "What is a horseshoe crab?"
"""

# # Use subprocess.run to execute the command
# # Shell=True is used to interpret the command as a string and execute it through the shell
# # This is necessary for commands that involve shell operators like '&&'
possible_exception = ""

try:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

except Exception as e:
    possible_exception = str(e)

# # Print the standard output and error (if any)
# print("STDOUT:", result.stdout)
# print("STDERR:", result.stderr)

# # Check the return code (0 usually means success)
# if result.returncode == 0:
#     print("Command executed successfully")
# else:
#     print("Command failed with return code", result.returncode)

# print(f"result.returncode=={result.returncode}-")


if result.returncode == 0:
    print("command_executed_successfully_finis")

    # Assuming valid output means non-empty stdout
    if result.stdout.strip():
        #####################################
        # Look for Standard Ouput (no error)
        #####################################
        
        
        # Valid output received; print the standard output
        # print(f"result.returncode=={result.returncode}--Assisant: ")
        # print(result.stdout)
        
        status_message = f"status_message=OK"
        
        # The model's output
        model_output = result.stdout
        
        # Make a tuple of
        ok_output_tuple = (result.returncode, status_message, model_output)
        
        print(ok_output_tuple)
        
    else:
        ##################################
        # Look for Standard Error message
        ##################################
        
        # No valid output; check if there's an error message
        if result.stderr.strip():
            # Print the standard error if error info is available
            status_message = f"ERROR: An error occured. {possible_exception}"
            
            print("STDERR:", result.stderr)
            ok_output = (result.returncode, result.stdout)
            
        else:
            # No output and no error; might indicate an unexpected issue or simply no output for the input
            status_message = "Strange: No output and no detected errors."
            not_ok_output_tuple = (result.returncode, status_message)
      

elif result.returncode != 0:
                         
    print("Error: Command failed with return code -> ", result.returncode)
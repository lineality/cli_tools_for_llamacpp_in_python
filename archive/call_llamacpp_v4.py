

# gpt4 OpenAI
import subprocess


def api_llamacapp(prompt, parameter_dict=[]):
    """
    requires:
        subprocess
    
    function/script code in python to make use of llama.cpp cli
    in project pipelines,
    e.g. to swap-in for another API (public cloud, not private)
    e.g. to use a local mode instead of an online-api (local, offline, private)
    """
    
    
    # Define the command as a string
    command = f"""
    make -j && ./main 2>/dev/null -m /home/oops/jan/models/tinyllama-1.1b/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf -p "What is a horseshoe crab?"
    """

    # Define the command as a string
    command = f"""
    ./main 2>/dev/null -m /home/oops/jan/models/tinyllama-1.1b/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf -p "What is a horseshoe crab?"
    """


    possible_exception = ""

    
    #################################
    # Try to Run Model, Prompt Model
    #################################
    """
    Use subprocess.run to execute the ~bash cli command
    Shell=True is used to interpret the command as a string and execute it through the shell
    This is necessary for commands that involve shell operators like '&&'
    
    make -j && ./main 2>/dev/null -m /home/oops/jan/models/tinyllama-1.1b/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf -p "What is a horseshoe crab?"
    
    ./main 2>/dev/null -m /home/oops/jan/models/tinyllama-1.1b/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf -p "What is a horseshoe crab?"
    
    """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

    except Exception as e:
        possible_exception = str(e)


    #######################################
    # Examine and Handle Attpted Model Use
    #######################################
    
    # get return coce (zero means no error, 1 or other means error)
    return_code_zero_means_ok = result.returncode
    
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
            
            # get return coce (zero means no error, 1 or other means error)
            return_code_zero_means_ok = result.returncode
            
            # Write a custom status message
            status_message = f"status_message=OK"
            
            # The model's output
            model_output = result.stdout
            
            # Make a tuple of output data for granular separate use
            ok_output_tuple = (return_code_zero_means_ok, status_message, model_output)
            
            # pseudo return
            return ok_output_tuple
            
        else:
            ##################################
            # Look for Standard Error message
            ##################################
            
            # No valid output; check if there's an error message
            if result.stderr.strip():
                # Print the standard error if error info is available
                status_message = f"ERROR: An error occured. {possible_exception}"
                
                # The model's ERROR output
                model_output = f"STDERR: {result.stderr}"

                # Make a tuple of output data for granular separate use
                not_ok_output_tuple = (return_code_zero_means_ok, status_message, model_output)
                
                # pseudo return
                return not_ok_output_tuple                
                                                
            else:  # No error reported, BUT no output either !!
                
                # No output and no error; might indicate an unexpected issue or simply no output for the input
                status_message = f"Strange: No output and no detected errors. {possible_exception}"
                
                # No error reported, BUT no output either 
                model_output = "blank"
                
                # Make a tuple of output data for granular separate use                
                not_ok_output_tuple = (return_code_zero_means_ok, status_message, model_output)
        
                # pseudo return
                return not_ok_output_tuple

    elif result.returncode != 0:
                                    
        # No output and no error; might indicate an unexpected issue or simply no output for the input
        status_message = f"Error: Command failed with return code -> {possible_exception}"
        
        if result.stderr.strip():
            # The model's ERROR output
            model_output = f"STDERR: {result.stderr}"
        else:
            # No error reported, BUT no output either 
            model_output = f"No standard output or STDERR standard error"
        
        # Make a tuple of output data for granular separate use                
        not_ok_output_tuple = (return_code_zero_means_ok, status_message, model_output)

        # pseudo return
        return not_ok_output_tuple
        
######
# Use
######

prompt = "What is a horseshoe crab?"

result = api_llamacapp(prompt, parameter_dict=[])

# get third part of tuple
exit_code = result[0]
message = result[1]
assistant_says = result[2]

print(exit_code)
print(message)
print(assistant_says)
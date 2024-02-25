# gpt4 OpenAI
import subprocess

def api_llamacapp(prompt, cpp_path, model_path_base, model_name, parameter_dict=[]):
    """
    requires:
        import subprocess
    
    function/script code in python to make use of llama.cpp cli
    in project pipelines,
    e.g. to swap-in for another API (public cloud, not private)
    e.g. to use a local mode instead of an online-api (local, offline, private)
    
    """
    
    ###
    # Parameters
    ###
    
    parameter_string = ""
    
    #######################################
    # Construct string of extra parameters
    ########################################
    for key, value in parameter_dict.items():
        
        # There will be a key, so add it in
        parameter_string += (str(key) + " ")
        
        # if there is a value, add that too
        if value:
            parameter_string += (str(value) + " ")
    
    
    whole_model_path = model_path_base + model_name
    
    # Define the command as a string
    command = f"""
    make -j && ./main 2>/dev/null -m {whole_model_path} --prompt "{prompt}"
    """

    # Define the command as a string
    command = f"""
    ./main 2>/dev/null -m {whole_model_path} --prompt "{prompt}"
    """

    # inspection
    # print(f"command -> {command}")

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
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=cpp_path)


        

    except Exception as e:
        possible_exception = str(e)


    #######################################
    # Examine and Handle Attpted Model Use
    #######################################
    
    # get return coce (zero means no error, 1 or other means error)
    return_code_zero_means_ok = result.returncode
    
    if result.returncode == 0:

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
            status_message = f"status_message: OK!!"
            
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
        
##############
# Setup Layer
##############

def prompt_setup_llamacpp(prompt):
    parameter_dict = {
        '--temp N': 0.8, # (default value is 0.8)
        '--top-k': 40,   # (selection among N most probable. default: 40)
        '--top-p': 0.9,  # (probability above threshold P. default: 0.9)
        '--min-p': 0.05, # (minimum probability threshold. default: 0.05)
        '--seed': -1,    # seed, =1 is random seed
        '--tfs': 1,	     # (tail free sampling with parameter z. default: 1.0) 1.0 = disabled
        '--threads': 8,     # (~ set to number of physical CPU cores)
        '--typical': 1,	# (locally typical sampling with parameter p  typical (also like ~Temperature) (default: 1.0, 1.0 = disabled).
        '--mirostat': 2, # (default: 0,  0= disabled, 1= Mirostat, 2= Mirostat 2.0)
        '--mirostat-lr': 0.05,  # (Mirostat learning rate, eta.  default: 0.1)
        '--mirostat-ent': 3.0,  # (Mirostat target entropy, tau.  default: 5.0)
        '--ctx-size': 500      # Sets the size of the prompt context
        }

    model_path_base = "/home/oops/jan/models/"
    model_name = "tinyllama-1.1b/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
    cpp_path = "/home/oops/code/llama_cpp/llama.cpp"

    result = api_llamacapp(prompt, cpp_path, model_path_base, model_name, parameter_dict)

    # get third part of tuple
    exit_code = result[0]
    message = result[1]
    assistant_says = result[2]

    # print(f"exit_code - > {exit_code}")
    # print(f"message - > {message}")
    # print(f"assistant_says - > {assistant_says}")

    return assistant_says
    
    
def jan_model_history_local_gguf_api(this_model, converstion_history):
    
    
    #######################
    # Tune Your Paramaters
    #######################
    parameter_dict = {
        '--temp N': 0.8, # (default value is 0.8)
        '--top-k': 40,   # (selection among N most probable. default: 40)
        '--top-p': 0.9,  # (probability above threshold P. default: 0.9)
        '--min-p': 0.05, # (minimum probability threshold. default: 0.05)
        '--seed': -1,    # seed, =1 is random seed
        '--tfs': 1,	     # (tail free sampling with parameter z. default: 1.0) 1.0 = disabled
        '--threads': 8,     # (~ set to number of physical CPU cores)
        '--typical': 1,	# (locally typical sampling with parameter p  typical (also like ~Temperature) (default: 1.0, 1.0 = disabled).
        '--mirostat': 2, # (default: 0,  0= disabled, 1= Mirostat, 2= Mirostat 2.0)
        '--mirostat-lr': 0.05,  # (Mirostat learning rate, eta.  default: 0.1)
        '--mirostat-ent': 3.0,  # (Mirostat target entropy, tau.  default: 5.0)
        '--ctx-size': 500      # Sets the size of the prompt context
        }

    # set your local jan path
    model_path_base = "/home/oops/jan/models/"
    
    
    model_name = "tinyllama-1.1b/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
    
    
    cpp_path = "/home/oops/code/llama_cpp/llama.cpp"

    result = api_llamacapp(prompt, cpp_path, model_path_base, model_name, parameter_dict)

    # get third part of tuple
    exit_code = result[0]
    message = result[1]
    assistant_says = result[2]

    # print(f"exit_code - > {exit_code}")
    # print(f"message - > {message}")
    # print(f"assistant_says - > {assistant_says}")

    return assistant_says
    
    

    
            
######
# Use
######

prompt = "What is a horseshoe crab?"

assistant_reponds = prompt_setup_llamacpp(prompt)

# print(type(assistant_reponds))
print(assistant_reponds)



conversation_history = [
{"role": "system", "content": user_input},
{"role": "user", "content": user_input},
{"role": "assistant", "content": user_input},
{"role": "user", "content": user_input},
{"role": "assistant", "content": user_input},
{"role": "user", "content": user_input},
]

# Define the request body
request_body = {
  "model": "mistral-small",  # 'mistral-small' is 8x7, vs. 'mistral-tiny' for 7b
  "messages": conversation_history
}

# Send the request
response = requests.post(endpoint_url, headers=headers, json=request_body)
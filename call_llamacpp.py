"""
Instructions:
1. Install Jan and download some models
2. Download any other models and put in the models folders in their own folders
3. Use this from anywhere, putting in the path to the models' folder

note:
There is a function to tell you what gguf models you already have and can pick from
You can use a shortened version of the model name.


Note:
Context-history looks like a big mystery...

TODO:
add a chat_llamacapp.py
using chat-context wrapper from Mixtral et all

"""


# gpt4 OpenAI
import subprocess
import os
    
def api_llamacapp(prompt, cpp_path, model_path_base, model_and_folder, parameter_dict=[]):
    """
    requires:
        import subprocess
    
    function/script code in python to make use of llama.cpp cli
    in project pipelines,
    e.g. to swap-in for another API (public cloud, not private)
    e.g. to use a local mode instead of an online-api (local, offline, private)
    
    """
    # # inspection
    # print("start")
    # print(f"""
    # prompt {prompt}, 
    # cpp_path {cpp_path}, 
    # model_path_base {model_path_base}, 
    # model_and_folder {model_and_folder}, 
    # parameter_dict {parameter_dict}
    # """)
    
    ######################
    # Make paths absolute
    ######################
    cpp_path = os.path.abspath(cpp_path)
    model_path_base = os.path.abspath(model_path_base)
    
    # make new path
    # Constructing the whole model path by joining the two parts
    whole_model_path = os.path.join(model_path_base, model_and_folder)
    # Make absolute
    whole_model_path = os.path.abspath(whole_model_path)
    
    #############
    # Parameters
    #############
    
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
    
    

    
    # Define the command as a string
    command = f"""
    make -j && ./main 2>/dev/null -m {whole_model_path} {parameter_string} --prompt "{prompt}"
    """

    # Define the command as a string
    command = f"""
    ./main 2>/dev/null -m {whole_model_path} {parameter_string} --prompt "{prompt}"
    """

        # Define the command as a string
    command = f"""
    ./main 2>/dev/null -m {whole_model_path} -p "{prompt}"
    """
    
    # # inspection
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

    prompt = str(converstion_history)    
    
    result = api_llamacapp(prompt, cpp_path, model_path_base, model_name, parameter_dict)

    # get third part of tuple
    exit_code = result[0]
    message = result[1]
    assistant_says = result[2]

    # print(f"exit_code - > {exit_code}")
    # print(f"message - > {message}")
    # print(f"assistant_says - > {assistant_says}")

    return assistant_says
    
def call_ggug_modelname_history(model_nickname, converstion_history):

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
    
    model_path = get_model_path_by_name(model_path_base, model_nickname)
    
    print(model_path)
    
    cpp_path = "/home/oops/code/llama_cpp/llama.cpp"
    
    prompt = f"{sanitize_for_bash(str(converstion_history))}"
    result = api_llamacapp(prompt, cpp_path, model_path_base, model_path, parameter_dict)

    # get third part of tuple
    exit_code = result[0]
    message = result[1]
    assistant_says = result[2]

    # print(f"exit_code - > {exit_code}")
    # print(f"message - > {message}")
    # print(f"assistant_says - > {assistant_says}")

    return assistant_says
    


"""
For use with Jan or another directory of models,
this will return a list of optional gguf model-paths
for the llama-cpp api
"""

import os

def find_folders_and_files_with_gguf(base_path):
    folders_and_files_with_gguf = []
    # Iterate through all items in base path
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Check each file in the directory
            for file in os.listdir(item_path):
                # Check if the file ends with '.gguf'
                if file.endswith('.gguf'):
                    # Construct the desired string format: basefolder/filename
                    result = f"{item}/{file}"
                    folders_and_files_with_gguf.append(result)
                    break  # Found a matching file, no need to check the rest
    return folders_and_files_with_gguf

# Base path where to search for folders and gguf files
# base_path = '/home/oops/jan/models'

# # Call the function and print the result
# folders_and_files = find_folders_and_files_with_gguf(base_path)
# for result in folders_and_files:
#     print(f"Model @->  {result}")

def sanitize_for_bash(input_str):
    """
    Sanitize a string by replacing curly braces, square brackets, and double quotes
    with parentheses and single quotes to avoid bash conflicts.

    Args:
    - input_str (str): The input string to be sanitized.

    Returns:
    - str: The sanitized string.
    """
    # Replace curly braces and square brackets with parentheses
    sanitized_str = input_str.replace('{', '(').replace('}', ')')
    sanitized_str = sanitized_str.replace('[', '(').replace(']', ')')
    sanitized_str = sanitized_str.replace('[', '(').replace(']', ')')
    

    # experimental:
    sanitized_str = sanitized_str.replace("""'role': 'system', 'content'""", 'Instruction you must follow')
    sanitized_str = sanitized_str.replace("""'role': 'assistant', 'content'""", 'Then you said')
    sanitized_str = sanitized_str.replace("""'role': 'user', 'content'""", 'Then I said')
    
    # Replace double quotes with single quotes
    sanitized_str = sanitized_str.replace('"', "'")

    return sanitized_str


def get_model_path_by_name(base_path, model_name):
    # Call the function to get all folders and files with gguf
    folders_and_files = find_folders_and_files_with_gguf(base_path)
    
    # Filter results by model name
    matching_models = [path for path in folders_and_files if model_name in path]
    
    # Check the number of matches and return accordingly
    if len(matching_models) == 1:
        # # inspection
        # print(matching_models[0])
        
        return matching_models[0]
    elif len(matching_models) > 1:
        raise "Error: More than one model found matching the given name. Please be more specific."
    else:
        raise "Error: No models found matching the given name."

# # Example usage
# base_path = '/home/oops/jan/models'
# model_name = input("Please enter the model name you are looking for: ")
# model_path = get_model_path_by_name(base_path, model_name)

# print(model_path)

            
####################
# Use direct prompt
####################
# prompt = "What is a horseshoe crab?"
# assistant_reponds = prompt_setup_llamacpp(prompt)
# # print(type(assistant_reponds))
# print(assistant_reponds)


#############################
# Use model select + history
#############################
conversation_history = [
{"role": "system", "content": "You are a friendly assistant."},
{"role": "user", "content": "Is cooking easy?"},
{"role": "assistant", "content": "Yes, it is. What shall we cook?"},
{"role": "user", "content": "Let's make bread."},
{"role": "assistant", "content": "Here is a good cornbread recipe..."},
{"role": "user", "content": "What are we cooking?"},
]

# Define the request body
request_body = {
  "model": "mistral-small",  # 'mistral-small' is 8x7, vs. 'mistral-tiny' for 7b
  "messages": conversation_history
}

# Send the request
# response = requests.post(endpoint_url, headers=headers, json=request_body)

# conversation_history = "What is a horseshoe crab?"

# response = call_ggug_modelname_history(model_nickname, converstion_history)
response = call_ggug_modelname_history("tinyllama", conversation_history)

print(response)
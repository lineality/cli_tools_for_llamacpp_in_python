from call_llamacpp import get_model_path_by_name

"""
'model_path_base': "/home/oops/jan/models/",
'model_nickname': f{use_this_model},
# /home/oops/jan/models/mistral-ins-7b-q4/mistral-7b-instruct-v0.2.Q4_K_M.gguf
"""


model_name = input("Model name is...")

model_path_base = "/home/oops/jan/models/"

result = get_model_path_by_name(model_path_base, model_name)

print(result)

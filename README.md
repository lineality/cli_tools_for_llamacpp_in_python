# cli_tools_for_llamacpp_in_python

Preliminary tools for using llama.cpp e.g. selecting a model and using
a local gguf model instead of a paid cloud api.

#### Notes:
- system prompts and conversation history 'context' are still not clear, not well implimented yet. 


- save history as...file?
- read in file as instruct?
(separate files to avoid formatting issues?
- 
sample:
translate 'sign up' into french, with your translation between pipes |translation| and other commentary outside

# To use:
1. close repo and cd inside (cd -> change directory)
2. set path_to_model_foler as it exists on your system
3. Run:
```python
python call_llamacapp.py
```


# TODO
- maybe make an instruct...doc maker reader...thing
- convert from csv to jsonl?
- maybe convert csv to dict (like json to dict) to handle questions?
- 



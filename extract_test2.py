def extract_dictionaries_from_string_no_pips(input_string):

    input_string = input_string.replace("\n","")

    pattern = r'{.*?}'
    matches = re.findall(pattern, input_string)
    dictionaries = []

    for match in matches:
        try:
            dictionary = eval(match)
            if isinstance(dictionary, dict):
                dictionaries.append(dictionary)
        except (SyntaxError, NameError, TypeError):
            pass

    return dictionaries



def return_list_of_jsons_from_string(dict_str):

    try:


        if "`" in str(dict_str):
            dict_str = dict_str.replace("\n", " ")

            # Define the pattern to match JSON blocks enclosed in triple backticks
            pattern = r'```json(.*?)```'
            matches = re.finditer(pattern, dict_str)

            # Initialize an empty list to store extracted JSON strings
            json_blocks = []

            for match in matches:
                # Extract the JSON string from the match and append it to the list
                json_blocks.append(match.group(1))

            # Return the list of JSON strings
            return json_blocks[-1]


        else:
            # try without pips
            print("try extract_dictionaries_from_string_no_pips(dict_str) ")
            return extract_dictionaries_from_string_no_pips(dict_str)

    except:
        print(f"failed, no json return_list_of_jsons_from_string(dict_str) dict_str-> {dict_str}")
        return False


# Helper Function
def json_number_check_structure_of_response_to_list(dict_str) -> list:
    """
    This function CAN fail and should fail
    if the AI needs to retry at a task.
    Do not stop server when this this triggers an exception.

    edge case: before there is a populated output_log

    if passing, this function will return a valid json object
    """

    """
    1. Extracts JSON string enclosed between ```json and ``` markers.

    2. extracts values from the dict

    Parameters:
    - text (str): The input text containing the JSON block.

    Returns:
    - str: The extracted JSON string, or an empty string if no JSON block is found.
    """
    print(f"\n\n json_number_check_structure_of_response_to_list -> {repr(dict_str)} \nType -> {type(dict_str)}")

    if "'" in str(dict_str):
        extracted_dict = return_list_of_jsons_from_string(dict_str)
        print(f"extracted_dict {extracted_dict}")
        print(f"type(extracted_dict) {type(extracted_dict)}")

    else:
        result = extract_dictionaries_from_string_no_pips(dict_str)
        # get last item
        extracted_dict = result[-1]


    if not extracted_dict:
        return False

    number_list = extract_values_from_dict(extracted_dict) 

    print(f"\n  final extracted from markdown, dict, etc. number_list ->{repr(number_list)}")

    # if ok...
    return number_list

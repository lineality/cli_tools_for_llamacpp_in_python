import json
import re
# Helper Function
def json_number_check_structure_of_response(dict_str):

    # extraction 1
    try:
        if "'''json" in dict_str:
            pattern = r"'''json\n([\s\S]*?)\n'''"
            match = re.search(pattern, dict_str)

            if match:
                print("\nMATCH!")
                # Extract the matched group, which contains the JSON string
                dict_str = match.group(1)
                print(dict_str)
            else:
                dict_str = ""

        else:
            print("'''json NOT FOUND")

    except Exception as e:
        print(
            f"\nTRY AGAIN: check_structure_of_response() extraction from markdown failed: {e}"
        )
        print(f"Failed dict_str -> {repr(dict_str)}")
        return False


    # load
    try:
        # try converting
        print(f"dict_str -> {repr(dict_str)} {type(dict_str)}")

        # Load the string into a Python dictionary
        dict_data = json.loads(dict_str)

    except Exception as e:
        print(f"\nTRY AGAIN: trying json.loads(dict_str) Dictionary load failed: {e}")
        print(f"Failed repr(dict_str) -> {repr(dict_str)}")
        return False

    # extraction 2
    try:
        # Extract the value associated with the key 'translation'
        dict_str = extract_values(dict_data)



    except Exception as e:
        print(
            f"\nTRY AGAIN: check_structure_of_response() extraction 2 from translation = dict_data['translation'] failed: {e}"
        )
        print(f"Failed repr(dict_str) -> {repr(dict_str)}")
        return False

    # try:
    #     # if test fails
    #     if dict_leaf_detection_boolean_true_means_defective(dict_str):
    #         return False

    # except Exception as e:
    #     print(f"\nTRY AGAIN: dict_leaf_detection_boolean_true_means_defective() empty or stub leaf found: {e}")
    #     print(f"Failed dict_str -> {dict_str}")
    #     return False

    print(f"\n  final extracted from markdown, dict, etc. ->{repr(dict_str)}")

    # if ok...
    return dict_str



input = """
Evaluate (0-10, 0 is terrible, 10 is great) each German translation for 'your account name' from these options: {'your_translation': 'score_here', 'Dein Benutzername': 'score_here'}. Place your evaluations as a value to the key in Json format. Return your markdown json object listing each translation only as t-number as: '''json {'t-1': 'score_here', 't-2': 'score_here', 't-3': 'score_here'} ''' No additional comments. A tasty reward awaits your accurate selection.

'''json {
  "t-1": "0",
  "t-2": "10"
}
''' The first translation is not German, so I will give a score of 0 for it. The second one, 'Dein Benutzername', translates directly to 'Your user name' in English and should receive a score of 10. Therefore:

'''json {
  "t-1": "0",
  "t-2": "10"
}
'''
0
status_message: OK!!
 Evaluate (0-10, 0 is terrible, 10 is great) each German translation for 'your account name' from these options: {'your_translation': 'score_here', 'Dein Benutzername': 'score_here'}. Place your evaluations as a value to the key in Json format. Return your markdown json object listing each translation only as t-number as: '''json {'t-1': 'score_here', 't-2': 'score_here', 't-3': 'score_here'} ''' No additional comments. A tasty reward awaits your accurate selection.

'''json {
  "t-1": "0",
  "t-2": "10"
}
''' The first translation is not German, so I will give a score of 0 for it. The second one, 'Dein Benutzername', translates directly to 'Your user name' in English and should receive a score of 10. Therefore:

'''json {
  "t-1": "0",
  "t-2": "10"
}
'''

"""


print( json_number_check_structure_of_response(input) )
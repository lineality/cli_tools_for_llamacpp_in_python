import os

def get_absolute_base_path():
    # Get the absolute path to the current user's home directory (Starts from root, ends at home directory)
    home_directory = os.path.expanduser("~")  # e.g., "/home/john"

    # # Define your relative path (Starts from home directory, ends at your target file/directory)
    # relative_path = "Documents/my_project/config.txt"  # e.g., "Documents/my_project/config.txt"

    # # Create an absolute path (Starts from root, ends at your target file/directory)
    # absolute_path = os.path.join(home_directory, relative_path)  # e.g., "/home/john/Documents/my_project/config.txt"

    absolute_path = os.path.abspath(home_directory)

    return absolute_path

print(get_absolute_base_path())


def add_segment_to_absolute_base_path(additional_segment):

    # Get the absolute path to the current user's home directory (Starts from root, ends at home directory)
    home_directory = os.path.expanduser("~")  # e.g., "/home/john"

    # Create an absolute path including the new segment
    absolute_path = os.path.join(home_directory, additional_segment)

    absolute_path = os.path.abspath(absolute_path)

    return absolute_path


print(add_segment_to_absolute_base_path("/jan/models"))


def add_segment_to_absolute_base_path(additional_segment):
    # Get the absolute path to the current user's home directory
    home_directory = os.path.expanduser("~")
    print(f"Home Directory: {home_directory}")  # Debugging print

    # Create an absolute path by joining the home directory with the additional segment
    absolute_path = os.path.join(home_directory, additional_segment)
    print(f"Joined Path Before abspath: {absolute_path}")  # Debugging print

    # Ensure the path is absolute (this should not change the path if already absolute)
    absolute_path = os.path.abspath(absolute_path)
    print(f"Final Absolute Path: {absolute_path}")  # Debugging print

    return absolute_path

# Example usage
absolute_path_result = add_segment_to_absolute_base_path("jan/models/")
print(f"Result: {absolute_path_result}")
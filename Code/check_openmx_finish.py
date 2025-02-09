import os

def check_files(directory="."):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".std") and filename.startswith("openmx"):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, "r") as file:
                        last_line = None
                        for line in file:
                            last_line = line.strip()
                        if last_line == "The calculation was normally finished.":
                            print(f"File {file_path}: Check Passed")
                        else:
                            print(f"File {file_path}: Check Failed")
                except Exception as e:
                    print(f"Error reading file {file_path}: {str(e)}")

check_files()
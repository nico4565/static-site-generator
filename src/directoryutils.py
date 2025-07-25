import shutil
import os


def clean_and_clone(destination_folder, origin_folder):
    # Remove destination folder if it exists
    if os.path.exists(destination_folder):
        print("start clean...")
        shutil.rmtree(destination_folder)

    # Recreate destination folder
    os.makedirs(destination_folder)

    # Copy contents from origin to destination
    for element in os.listdir(origin_folder):
        print("start clone..")
        origin_path = os.path.join(origin_folder, element)
        dest_path = os.path.join(destination_folder, element)

        if os.path.isfile(origin_path):
            shutil.copy(origin_path, dest_path)
        elif os.path.isdir(origin_path):
            clean_and_clone(dest_path, origin_path)
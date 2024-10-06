import argparse
import os
import shutil
def create_file_structure(output_folder, dataset_folder):
    os.makedirs(output_folder, exist_ok=True)
    data_folder = os.path.join(output_folder, "Data")
    os.makedirs(data_folder, exist_ok=True)
    for subfolder in ["train", "test", "validation"]:
        src = os.path.join(dataset_folder, subfolder)
        dst = os.path.join(data_folder, subfolder)
        if os.path.exists(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            print(f"Warning: {src} not found in the dataset folder.")
    for file in ["main.py", "model.py", "utils.py", "train.py", "test.py"]:
        with open(os.path.join(output_folder, file), "w") as f:
            pass
    with open(os.path.join(output_folder, "test_notebook.ipynb"), "w") as f:
        f.write('{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 4}')
def main():
    parser = argparse.ArgumentParser(description="Create file structure for ML project")
    parser.add_argument("command", help="Command to execute (e.g., 'create')")
    parser.add_argument("output_folder", help="Path to the output folder")
    parser.add_argument("dataset_folder", help="Path to the folder containing dataset images")
    args = parser.parse_args()
    if args.command.lower() == "create":
        create_file_structure(args.output_folder, args.dataset_folder)
        print(f"File structure created successfully in {args.output_folder}")
    else:
        print(f"Unknown command: {args.command}")
if __name__ == "__main__":
    main()

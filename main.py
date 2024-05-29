import shutil
import os

def copy_and_move_all_videos(src_dir_path, dest_dir_path, new_file_prefix):
    """
    Copies all video files from the source directory to the destination directory,
    renaming them with a new prefix.

    :param src_dir_path: str, the source directory path
    :param dest_dir_path: str, the destination directory path
    :param new_file_prefix: str, the new file prefix
    :return: None
    """
    if not os.path.isdir(src_dir_path):
        raise NotADirectoryError(f"The source directory does not exist: {src_dir_path}")

    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    for i, filename in enumerate(os.listdir(src_dir_path)):
        src_file_path = os.path.join(src_dir_path, filename)
        
        if os.path.isfile(src_file_path) and filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            new_file_name = f"{new_file_prefix}_{i}{os.path.splitext(filename)[1]}"
            dest_file_path = os.path.join(dest_dir_path, new_file_name)
            
            shutil.copy(src_file_path, dest_file_path)
            print(f"File copied from {src_file_path} to {dest_file_path}")

# Get user input for paths and prefix
src_dir = input("Enter the source directory path: ")
dest_dir = input("Enter the destination directory path: ")
new_prefix = input("Enter the new file prefix: ")

copy_and_move_all_videos(src_dir, dest_dir, new_prefix)

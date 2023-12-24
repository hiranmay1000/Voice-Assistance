import os

def get_log_file_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "../logs/log_file.txt")

def get_assets_file_path(file_path):
    media_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(media_dir, file_path)
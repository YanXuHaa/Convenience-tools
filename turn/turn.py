import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

source_folder = 'input_webm'
target_folder = 'output'
print("    Running Turn.py ........")

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

def get_frame_rate(webm_file_path):
    command = ['ffprobe', '-v', '0', '-of', 'csv=p=0', '-select_streams', 'v', '-show_entries', 'stream=r_frame_rate', webm_file_path]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error getting frame rate for {webm_file_path}: {result.stderr}")
        return None
    return result.stdout.strip()

def convert_webm_to_gif(filename):
    webm_file_path = os.path.join(source_folder, filename)
    gif_file_path = os.path.join(target_folder, filename[:-4] + 'gif')

    frame_rate = get_frame_rate(webm_file_path)
    if frame_rate is None:
        return

    command = [
        'ffmpeg', '-i', webm_file_path, '-vf', f"fps={frame_rate}", gif_file_path
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error converting {filename} to GIF: {result.stderr}")
    else:
        print("     Done!")

num_threads = os.cpu_count() or 8  

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    for filename in os.listdir(source_folder):
        if filename.endswith('.webm'):
            executor.submit(convert_webm_to_gif, filename)
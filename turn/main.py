import os
import subprocess
from termcolor import colored
import sys
input_folder = 'input'
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
output_folder = 'output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
print(colored('LaunchSystem：CheckSystem will be launch', 'yellow'))
class Error43(Exception):
    pass

check_folder = 'input'
files = os.listdir(check_folder)
allowed_extensions = ['.webp', '.webm']

for file in files:
    extension = os.path.splitext(file)[1].lower()
    if extension not in allowed_extensions:
        file_path = os.path.join(check_folder, file)
        print(colored(f'  CheckSystem：Error7: {file} Have something wrong.', 'red'))
        print(colored(f'  CheckSystem：Check Error,Try to auto fix', 'red'))
        print(colored(f'  CheckSystem：AutoFixSystem will be launch', 'red'))
        print(colored(f'   AutoFixSystem：ReFinding Error.....', 'magenta'))
        print(colored(f'   AutoFixSystem：Find!,The error has been recorded', 'magenta'))
        print(colored(f'   AutoFixSystem：Looking up the way to fix', 'magenta'))
        print(colored(f'   AutoFixSystem：Trying to fix', 'magenta'))
        os.remove(file_path)
        print(colored(f'   AutoFixSystem：Done!', 'magenta'))
        print(colored(f'  CheckSystem：ReChecking.......', 'blue'))
try:
    if not os.listdir(input_folder):
        print(colored('  CheckSystem：Error4:No any files in Input', 'red'))
        print(colored(f'  CheckSystem：Check Error,Try to auto fix', 'red'))
        print(colored(f'  CheckSystem：AutoFixSystem will be launch', 'red'))
        print(colored(f'   AutoFixSystem：ReFinding Error.....', 'magenta'))
        print(colored(f'   AutoFixSystem：Find!,The error has been recorded', 'magenta'))
        print(colored(f'   AutoFixSystem：Looking up the way to fix', 'magenta'))
        print(colored(f'   AutoFixSystem：The Error CAN NOT be fix,Because It is the user that causes the problem.', 'magenta'))
        raise Error43(colored('LaunchSystem：All system will be shutdown', 'yellow'))
except Error43 as e:
    print(e)
    sys.exit(1)
print(colored('  CheckSystem：Check Done! MainSystem can be launch','blue'))
print(colored('LaunchSystem：MainSystem will be launch', 'yellow'))
# 运行pretreatment.py
print(colored(' MainSystem：PretreatmentSystem will be launch', 'green'))
subprocess.run(['python', 'pretreatment.py'], check=True)
print(colored(' MainSystem：AutoRunSystem will be launch', 'green'))
# 检测input_webp文件夹
webp_folder = 'input_webp'
if os.listdir(webp_folder):  # 如果文件夹不为空
    # 执行turn1.py
    print(colored('   AutoRunSystem：Check done,Auto Run Turn1.py', 'blue'))
    subprocess.run(['python', 'turn1.py'], check=True)
    print(colored('   AutoRunSystem：turn1.py OK！', 'blue'))
else:
    print(colored('   AutoRunSystem：Check done,No .webp files,SKIP', 'blue'))

# 检测input_webm文件夹
webm_folder = 'input_webm'
if os.listdir(webm_folder):  # 如果文件夹不为空
    # 执行turn.py
    print(colored('   AutoRunSystem：Check done,Auto Run Turn.py', 'blue'))
    subprocess.run(['python', 'turn.py'], check=True)
    print(colored('   AutoRunSystem：turn.py OK！', 'blue'))
else:
    print(colored('   AutoRunSystem：Check done,No .webm files,SKIP', 'blue'))

input_webp_folder = 'input_webp'
input_webm_folder = 'input_webm'
try:
    for folder in [input_webp_folder, input_webm_folder]:
        if os.path.exists(folder):
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            os.rmdir(folder)
            print(colored(f' MainSystem：{folder} folder has been deleted successfully.', 'green'))
        else:
            print(colored(f' MainSystem：Error0: {folder} folder does not exist.', 'red'))
except Exception as e:
    print(colored(f' MainSystem：Error0: An error occurred while deleting folders: {e}', 'red'))


webm_folder = 'output'
if os.listdir(webm_folder):
   print(colored(' MainSystem：ALL DONE！', 'green'))
else:
    print(colored(' MainSystem：Error0:No Any Files output', 'red'))
    
print(colored('LaunchSystem：All system will be shutdown', 'yellow'))
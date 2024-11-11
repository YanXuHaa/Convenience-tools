import os
import shutil
print ("  Running pretreatment.py ........")
# 设置源文件夹和目标文件夹
source_folder = 'input'
webp_folder = 'input_webp'
webm_folder = 'input_webm'

# 确保目标文件夹存在，如果不存在则创建
if not os.path.exists(webp_folder):
    os.makedirs(webp_folder)
if not os.path.exists(webm_folder):
    os.makedirs(webm_folder)

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    # 获取文件的完整路径
    file_path = os.path.join(source_folder, filename)
    # 判断文件是否为webp或webm格式
    if filename.endswith('.webp'):
        # 移动webp文件到webp文件夹
        shutil.move(file_path, os.path.join(webp_folder, filename))
    elif filename.endswith('.webm'):
        # 移动webm文件到webm文件夹
        shutil.move(file_path, os.path.join(webm_folder, filename))

print("  PretreatmentSystem：Pretreatment Done")
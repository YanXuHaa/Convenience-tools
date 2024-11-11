from PIL import Image
import os

print ("    Running Turn1.py ........")
def convert_webp_to_png(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".webp"):
            # 构建完整的文件路径
            file_path = os.path.join(input_folder, filename)
            # 打开.webp文件
            with Image.open(file_path) as img:
                # 检查图片是否为静态图片
                if not img.is_animated:
                    # 生成输出文件路径
                    output_path = os.path.join(output_folder, filename[:-5] + ".png")
                    img.save(output_path, "PNG")
                    print ("     Done!")
input_folder = "input_webp"
output_folder = "output"
convert_webp_to_png(input_folder, output_folder)
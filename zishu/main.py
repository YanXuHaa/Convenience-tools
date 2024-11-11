import os
from docx import Document

# 定义一个函数来统计字符数
def count_characters(text):
    # 定义全角和半角标点符号的范围
    full_width_punctuations = '！＂＃＄％＆＇（）＊＋，－／：；＜＝＞？＠［＼］＾＿｀｛｜｝～'
    half_width_punctuations = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
    
    # 初始化计数器
    letter_count = 0
    full_width_punctuation_count = 0
    half_width_punctuation_count = 0
    
    # 遍历文本中的每个字符
    for char in text:
        # 检查是否是汉字或者英文字母
        if ('\u4e00' <= char <= '\u9fff') or char.isalpha():
            letter_count += 1
        # 检查是否是全角标点
        elif char in full_width_punctuations:
            full_width_punctuation_count += 1
        # 检查是否是半角标点
        elif char in half_width_punctuations:
            half_width_punctuation_count += 1
    
    return letter_count, full_width_punctuation_count, half_width_punctuation_count

# 初始化总字符数计数器
total_letters = 0
total_full_width_punctuation = 0
total_half_width_punctuation = 0

# 遍历input文件夹中的所有.docx文件
input_folder = 'input'
for filename in os.listdir(input_folder):
    if filename.endswith('.docx'):
        # 读取文档
        doc_path = os.path.join(input_folder, filename)
        doc = Document(doc_path)
        # 获取所有段落文本
        text = ''
        for paragraph in doc.paragraphs:
            text += paragraph.text
        
        # 计算字符数
        letters, full_width_punctuation, half_width_punctuation = count_characters(text)
        
        # 打印结果
        print(f"{filename}: \n汉字数={letters}, \n全角标点符号数={full_width_punctuation}, \n半角标点符号数={half_width_punctuation}\n")
        
        # 累加到总计数器
        total_letters += letters
        total_full_width_punctuation += full_width_punctuation
        total_half_width_punctuation += half_width_punctuation

# 打印总字符数
print(f"总计: 字母数（包括汉字和英文字母）={total_letters}, 全角标点符号数={total_full_width_punctuation}, 半角标点符号数={total_half_width_punctuation}")
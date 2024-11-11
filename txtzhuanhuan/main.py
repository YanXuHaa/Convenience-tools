import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os

input_folder = 'input'
output_txt_folder = 'output_txt'
output_picture_folder = 'output_picture'

if not os.path.exists(output_txt_folder):
    os.makedirs(output_txt_folder)
if not os.path.exists(output_picture_folder):
    os.makedirs(output_picture_folder)

for epub_file in os.listdir(input_folder):
    if epub_file.endswith('.epub'):
        epub_path = os.path.join(input_folder, epub_file)
        book = epub.read_epub(epub_path)
        
        epub_name = os.path.splitext(epub_file)[0]
        images_subfolder = os.path.join(output_picture_folder, epub_name)
        if not os.path.exists(images_subfolder):
            os.makedirs(images_subfolder)
        
        text = ''
        
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                soup = BeautifulSoup(item.content, 'html.parser')
                
                for img in soup.find_all('img'):
                    image_id = img['src']
                    if image_id.startswith('http://') or image_id.startswith('https://'):
                        continue
                    image_id = image_id.split('/')[-1]
                    image_item = book.get_item_with_id(image_id)
                    if image_item:
                        image_data = image_item.get_content()
                        image_path = os.path.join(images_subfolder, image_id)
                        with open(image_path, 'wb') as img_file:
                            img_file.write(image_data)
                        img['src'] = image_path
                        text += f'![Image]({image_path})\n'
                    else:
                        print(f"Warning: Image with ID {image_id} not found in the ePub file.")
                
                text += soup.get_text(separator=' ', strip=True) + '\n\n'
        
        txt_file_path = os.path.join(output_txt_folder, f'{epub_name}.txt')
        with open(txt_file_path, 'w', encoding='utf-8') as file:
            file.write(text)
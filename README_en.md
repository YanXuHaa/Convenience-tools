# Utility Tools
A repository for various aspects to facilitate my use of Android phone (Termux), storing various Python and Bash scripts.

# File Introduction
## turn folder and its files
*Requires termcolor & Pillow*

"turn" refers to conversion, in this code, it means converting webp and webm to jpg and gif for easier use.
(The code is filled with useless information display and useless processing, for reference only)
To use, place webp and webm files in the input folder, execute 'python main.py' to automatically convert and store them in the output folder.

## txtzhuanhuan folder and its files
*Requires ebooklib & beautifulsoup4*

"txtzhuanhuan" refers to converting to txt, in this code, it means converting epub format books to txt files and saving the photos separately.
To use, place epub format files in the input folder, execute 'python main.py' to automatically convert, photos will be placed in output picture, and text will be placed in output txt.

## zishu folder and its files
*Requires python-docx*

"zishu" refers to word count statistics, in this code, it means counting the total number of characters in .docx files in the input folder, allowing multiple .docx files, running 'python main.py' will give the total number of characters, Chinese characters, etc.

## Development Staff

1itt1e_1219 Wrote the entire code

## Log

2024/11/11
Added three tools: turn, txtzhuanhuan, and zishu.
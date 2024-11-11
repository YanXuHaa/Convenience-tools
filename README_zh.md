# 便利工具
一个关于各种方面的用于便利我自己使用安卓手机（termux）的仓库，存储各种python、bash


# 文件介绍
## turn文件夹及其文件
*需要termcolor&Pillow*

turn意指转换，在本代码中，即指将webp与webm转为jpg与gif，便于使用。
（代码内充斥无用的信息显示和无用的处理，仅供参考）
使用时需要将webp与webm文件放入input文件夹，执行'python main.py'即可自动转换后存放至output文件夹。

## txtzhuanhuan文件夹及其文件
*需要ebooklib&beautifulsoup4*

txtzhuanhuan意指转换为txt，在本代码中，即指将epub格式的图书转化为txt文件，并将其中照片额外保存。
使用时需要讲epub格式文件放入input文件夹,执行'python main.py'后即可自动转换后，照片放入output picture，文本放入output txt中

## zishu文件夹及其文件
*需要python-docx*

zishu意指字数统计，在本代码中，即指统计input文件夹内.docx文件总字数，允许多个.docx文件，运行'python main.py'后会给出包括总字符数、汉字数等。

## 开发人员

1itt1e_1219 全程编写

## 日志

2024/11/11
增加turn&txtzhuanhuan&zishu三个工具。

# f = open("test.txt", "w", encoding="utf-8")
# f.write("안녕, 스파르타! \n")
#
# for i in [1, 2, 3, 4, 5]:
#     f.write(f"{i}번째 줄이에요\n")
# f.close()
#
# text = ""
#
# with open("test.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     for line in lines:
#         text += line
#         # print(line, end="")
# print(text)

from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ''
with open("텍스트파", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if "] [" in line:
            text += line.split('] ')[2].replace('저', '').replace('저도', '').replace('저두', '').replace('ㅋ', '').replace('ㅠ', '').replace('이모티콘\n','').replace('사진\n','').replace('삭제된 메세지입니다.\n','')
# print(text)

# import matplotlib.font_manager일 as fm

# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)
# /System/Library/Fonts/Supplemental/AppleGothic.ttf

# wc = WordCloud(font_path="/System/Library/Fonts/Supplemental/AppleGothic.ttf", background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result.png")

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path="/System/Library/Fonts/Supplemental/AppleGothic.ttf", background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")
# -*- coding: utf-8 -*-
import jieba
import zhon.hanzi
import wordcloud
import PIL.Image as image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
punc = zhon.hanzi.punctuation
ifn = r"merge.txt"
ofn = r"train_output.txt"

infile = open(ifn, 'r')
outfile = open(ofn, 'w')

for line in infile.readlines():
    new=''.join([i for i in line if not i.isdigit()])
    outfile.write(new)

infile.close
outfile.close
new_words = ['机器学习', '计算机视觉', '自然语言处理', '深度学习']
for i in new_words:
		jieba.add_word(i)
stopwords = [line.strip() for line in open("cn_stopwords.txt",encoding="utf-8").readlines()]
with open('train_output.txt') as fp:
    text = fp.read()

ls = jieba.cut(text)

counts = {}
for i in ls:
    if len(i) > 2:
        counts[i] = counts.get(i, 0) + 1

for word in stopwords:
    counts.pop(word, 0)

ls = list(counts.items())
ls.sort(key= lambda x:x[1], reverse=True)
words=''
ans = open('ans.txt', 'w')
for i in range(90):
    word, count = ls[i]
    words=words+' '+word
    ans.write("{0:<10}{1:>5}".format(word, count)+'\n')

mask = np.array(image.open("1.png"))
wordcloud = WordCloud(font_path='C:/Windows/Fonts/simkai.ttf',mask=mask,background_color='#FFFFFF',scale=1).generate(words)

image_produce = wordcloud.to_image()

wordcloud.to_file("new_wordcloud.jpg")
image_produce.show()
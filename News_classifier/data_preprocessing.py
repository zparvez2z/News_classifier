import os
import codecs
import re
import time
start = time.time()
with codecs.open('news.txt','r',encoding='utf8') as f:
                text = f.read()
                print(len(text))

countRe = re.compile(r'\t')
print("no of tab before : "+str(len(countRe.findall(text))))


single_lined = re.sub(r'\s+', ' ', text)

countRe = re.compile(r'\t')
print("no of tab: "+str(len(countRe.findall(single_lined))))
tagged = re.sub(r'</news>\s+', '\t0\n', single_lined)

countRe = re.compile(r'\n')
print("no of newline: "+str(len(countRe.findall(tagged))))


countRe = re.compile(r'\t')
print("no of tab: "+str(len(countRe.findall(tagged))))

cleaned = re.sub(r'<date>|</date>|<title>|</title>|<news>','',tagged)


with codecs.open('news_out.tsv','w',encoding='utf8') as f:
    f.write(cleaned)


print("total time : "+str(time.time()-start))
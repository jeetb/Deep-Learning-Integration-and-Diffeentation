import os
with open('C://Users//YASH//Downloads//prim_fwd//preprocessed raw.test', 'r', encoding='utf-8') as f:
     lines = f.read().split('\n')

diff = open("diff.txt", "a+")
intg = open("intg.txt", "a+")

for i in lines:
    diff.writelines(i.split('\t')[0])
    intg.writelines(i.split('\t')[1])

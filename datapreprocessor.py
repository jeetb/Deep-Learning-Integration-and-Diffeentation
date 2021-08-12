with open('C://Users//YASH//Downloads//prim_fwd//preprocessed raw.test', 'r', encoding='utf-8') as f:
     lines = f.read().split('\n')
diff = []
intg = []

for i in lines[:-1]:
    line = i.split('\t')
    diff.append(line[0])
    intg.append(line[1])

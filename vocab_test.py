bert_set = set()
material_set = set()

with open(r'.\my.subword_text_encoder', 'r+',encoding='utf-8') as f:
    document=f.read().split('\n')
    for line in document:
        # print(line)
        material_set.add(line)

with open(r'.\vocab.txt', 'r+',encoding='utf-8') as f:
    document=f.read().split('\n')
    for line in document:
        # print(line)
        bert_set.add(line)

print(bert_set)
# print(material_set)
# complement_set=bert_set.difference(material_set)
complement_set=material_set.difference(bert_set)
print(complement_set)

with open(r'.\Complement.txt','w+',encoding='utf-8') as f:
    for item in complement_set:
        f.writelines(item+'\n')
word = input().upper()
dup_x = list(set(word))
ct_word = []
for x in dup_x :ct = word.count(x);ct_word.append(ct)
if ct_word.count(max(ct_word)) > 1:print('?')
else:max_index = ct_word.index(max(ct_word));print(dup_x[max_index])
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('總共有', len(data), '筆資料')

print(data[0])

# sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均長度是', sum_len/len(data))


# 篩選 小於一百字的留言

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度<100')

# 篩選有提到good的留言

good = []
for d in data:
	if 'good' in d:
		good.append(d)	
print('一共有', len(good), '筆留言提到good')
print(good[0])

# 另一種篩選快寫法
good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆留言提到good')


#文字計數
wc = {} #word count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Elaine'])

while True:
	word = input('請問你想查什麼字?')
	if word == 'q':
		break
	print(word, '出現過的次數為', wc[word])
print('感謝使用本查詢功能')

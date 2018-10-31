import hashlib

for i in range(10):
	for j in range(10):
		for k in range(10):
			for l in range(10):
				if (hashlib.sha1(("th" + str(i)+str(j)+str(k)+str(l)).encode()).hexdigest()) == "076DD1AD6A51FBC4B5F29692559E85302D51DF95".lower():
					print(str(i)+str(j)+str(k)+str(l))

#7731
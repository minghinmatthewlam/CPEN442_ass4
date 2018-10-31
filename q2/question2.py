import hashlib
values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="
for i in values:
	for j in values:
		for k in values:
			for l in values:
				for m in values:
					for n in values:
						if (hashlib.sha1(("us" + i+j+k+l+m+n).encode()).hexdigest()) == "5ECB838163CFD1D5CB560E720E26796B6B6E8B44".lower():
							print(i+j+k+l+m+n)


#usVXpVI3
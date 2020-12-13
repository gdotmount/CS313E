def grade(phrase, encode, decode):
	tree = Tree(phrase)

	try:
		encrypt = tree.encrypt(encode)
	except:
		encrypt = None

	try:
		if(encrypt != None):
			back_dec = tree.decrypt(encrypt)
		else:
			back_dec = None
	except:
		back_dec = None

	try:
		decrypt = tree.decrypt(decode)
	except:
		decrypt = None

	try:
		if(decrypt != None):
			back_enc = tree.encrypt(decrypt)
		else:
			back_enc = None
	except:
		back_enc = None

	consistent = back_enc != None and back_enc == decode and back_dec != None and back_dec == encode
	return encrypt, decrypt, consistent




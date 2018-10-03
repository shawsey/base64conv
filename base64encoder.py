#Base 64 Encoder 
#Written in Python
import string
#Step 1) ASCII --> DEC --> 8-BIT Binary
#collect plaintext, for letter in plaintext run through asciideclist until a match is found. 
#take match, jump one in index, will be equiv decimal of letter
#bin(i) to print the binary value of a decimal
def base64conv(plaintext):
	# plaintext = raw_input('Input string to decode: ')
	asciideclist = list(string.ascii_uppercase)
	#bin8 list for divisibility and bin6 conv
	bin8list = []
	bin6list = []
	#for letter in plaintext
	for i in plaintext:
		#loop through asciideclist until a match is found
		for c, value in enumerate(asciideclist, 1):
			#When match is found, take the index value of letter (1 - 26) and add to 64 base for decimal version
			if value == i:
				d =  (c + 64)
				#Change decimal to binary format, 8-bit				
				b = "{0:08b}".format(d)
				#append binary value to bin8list
				bin8list.append(b)
			else:
				pass
	#print(bin8list)
	#Find index count of bin8 list, and see if divisible by 6. 
	binlen =  len("".join(bin8list))
	#print (binlen)
	if  binlen % 6 != 0:
		opaddition = binlen % 6  
		#Opposite additions? 2 means add 4 0's and 4 means add 2 0's? Alright lol
		if opaddition == 2:
			bin8list.append('0000')
			#print("Addtion is 4")
		else:
			bin8list.append('00')
			print("Addition is 2")
	#print(bin8list)
	binlen =  len("".join(bin8list))
	binsectors = binlen / 6
	#print( binsectors)
	#Reformat 8bitbinlist into 6bitbinlist
	bincomblist = ("".join(bin8list))
	#print (bincomblist)
	n = 6 
	bin6list = [bincomblist[i:i+n] for i in range(0, binlen, n)]
	#print (bin6list)
	#Find decimal equivilent of 6-bit bin values
	declist = []
	for i in bin6list:
		b = int(i, 2)
		declist.append(b)
	#print(declist)
	asciiuplist = list(string.ascii_uppercase)
	asciilowlist = list(string.ascii_lowercase)
	numlist = [0,1,2,3,4,5,6,7,8,9]
	excaselist = ["+", "/"]
	base64text = []
	#Find ASCII Equivilent of decimal values
	for i in declist:
			if i <= 25:
				for c, value in enumerate(asciiuplist, 1):
					#When match is found, take the index value of letter (1 - 26) and add to 64 base for decimal version
					if c-1 == i:
						#append binary value to bin8list
						base64text.append(value)
					else:
						pass
			else:
				if 25 < i <= 51:
					for c, value in enumerate(asciilowlist, 1):
						#When match is found, take the index value of letter (1 - 26) and add to 64 base for decimal version
						if c+25 == i:
							#append binary value to bin8list
							base64text.append(value)
						else:
							pass
				else:
					if 51 < i <= 61:
						for c, value in enumerate(numlist, 1):
							#When match is found, take the index value of letter (1 - 26) and add to 64 base for decimal version
							if c+51 == i:
								#append binary value to bin8list
								base64text.append(value)
							else:
								pass
					else:
						if 61 < i < 64:
							for c, value in enumerate(excaselist, 1):
								#When match is found, take the index value of letter (1 - 26) and add to 64 base for decimal version
								if c+61 == i:
									#append binary value to bin8list
									base64text.append(value)
								else:
									pass
	#print(base64text)
	b64len =  len(base64text)
	#print(b64len)

	if  b64len % 4 != 0:
		opaddition = b64len % 4
		#print(opaddition) 
		#Opposite additions? 2 means add 4 0's and 4 means add 2 0's? Alright lol
		if opaddition == 2:
			base64text.append('==')
			#print("Addtion is 2")
		else:
			base64text.append('=')
			#print("Addition is 1")
	textstr = [str(i) for i in base64text]		
	encoded = ("".join(textstr))
	return encoded



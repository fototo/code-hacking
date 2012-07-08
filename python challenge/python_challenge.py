# http://www.pythonchallenge.com/


def c0():
	# http://www.pythonchallenge.com/pc/def/0.html
	print 2**38



def c1_helper(text):
	translated = []
	for letter in text:

		no = ord(letter)

		limit = 0
		if (no>=97-limit and no<=122-limit):
			if(no>=120):
				translated.append(chr(no+2-26))
			else:
				translated.append(chr(no+2))
		else:
			translated.append(chr(no))

	return ''.join(translated)

def c1():
	# http://www.pythonchallenge.com/pc/def/map.html
	# TODO: implement string.maketrans()

	text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
	
	print c1_helper(text)
	print c1_helper("map")
	

def c2():
	# http://www.pythonchallenge.com/pc/def/ocr.html
	f = open('c2.txt')
	text = f.read()
	f.close()

	charArray = ['\n', '*', '_', '}', '{', '[', ']', '&', '$', '#', ')', '(', 	'^', '!', '%', '+', '@']

	for c in charArray:
		text = text.replace(c,'')		
	

	print text



def c3():
	# http://www.pythonchallenge.com/pc/def/equality.html
	f = open('c3.txt')
	text = f.read()
	f.close()

	text = text.replace('\n','')

	result = []

	for i in range(len(text)-7):
		
		if text[i].islower():
			if text[i+1].isupper():
				if text[i+2].isupper():
					if text[i+3].isupper():
						if text[i+4].islower():
							if text[i+5].isupper():
								if text[i+6].isupper():
									if text[i+7].isupper():
										if text[i+8].islower():
											result.append(text[i+4: i+5])

	print ''.join(result)


def c4():
	# http://www.pythonchallenge.com/pc/def/linkedlist.php
	
	import urllib

	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'

	no = '12345'
	no = str(16044/2)
	no = '56523'
	no = '53548'
	no = '95493'
	no = '64814'
	no = '73355'
	no = '81905'
	no = '54827'
	no = '35959'
	no = '66831'


	while no != '' and no.isdigit():
		
		f = urllib.urlopen(url % no)
		data = f.read()
			
		no = data.split(' ')[-1]
		# and the next nothing is 56337
		print no, '==>', data
	
	f.close()


def c5():
	# http://www.pythonchallenge.com/pc/def/peak.html
	import pickle

	from pprint import pprint

	l = pickle.load( open( "banner.p", "rb" ) )

	for line in l:
		print ''.join(map(lambda pair: pair[0]*pair[1], line))


def fcont(_file):
	f = open(_file)
	data = f.read()
	f.close()
	return data


def c6():
	# http://www.pythonchallenge.com/pc/def/channel.html	
	# zip: http://www.pythonchallenge.com/pc/def/channel.zip	
	
	import zipfile
	
	no = '90052'
	file = zipfile.ZipFile("channel.zip", "r")

	result = []
	comment = []

	while no.isdigit():
		result.append(no)
		temp = file.read('%s.txt' % no)
	 	no = temp.split('Next nothing is ')[-1]
	
	print ''.join([file.getinfo(n+'.txt').comment for n in result])
		
		
def c7():
	# http://www.pythonchallenge.com/pc/def/oxygen.html

	import Image

	im = Image.open('oxygen.png')

	y = 0
	while True:
		p = im.getpixel((0, y))
		if p[0] == p[1] == p[2]:
			break
		y += 1

	x = 0
	while True:
		p = im.getpixel((x, y))
		if not (p[0] == p[1] == p[2]):
			break
		x += 1

	x_ini = 0
	x_fin = x-1
	y_ini = y
	
	vec = [chr(im.getpixel((i, y_ini))[0]) for i in range(x_ini, x_fin+1, 7)]
	print '==>', ''.join(vec)

	vec = [105, 110, 116, 101, 103, 114, 105, 116, 121]
	print '==>', ''.join([chr(v) for v in vec])


def c8():
	# http://www.pythonchallenge.com/pc/def/integrity.html
	import bz2

	un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
	pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
		
	print bz2.decompress(un)
	print bz2.decompress(pw)

def c9():
	# http://www.pythonchallenge.com/pc/return/good.html
	first = [146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,332,155,348,156,353,153,366,149,379,147,394,146,399]
	second = [156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159, 157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220, 125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162, 77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115, 158,121,157,128,156,134,157,136,156,136]

	import Image,ImageDraw
	im = Image.new('RGB', (500,500))
	draw = ImageDraw.Draw(im)


	draw.polygon(first,fill='white')
	draw.polygon(second,fill='white')
	im.save('09.jpg')



if __name__ == '__main__':
	c9()
	print 'done!'
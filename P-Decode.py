import itertools,sys,time,svg,_sha
from binascii import unhexlify , hexlify

'''

android pattern cracker v0.4

Coded by MGF15

file in android ->  /data/system/gesture.key

'''
logo =  '''
	|~)  |~\ _ _ _  _| _
	|~ ~~|_/}_(_(_)(_|}_ v0.4\n
		[ {41}ndr0id Pa77ern Cr4ck t00l. ]
	'''
now = time.time()
x_list = ["\x00","\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08"]
def crack(hash):

	print logo
	print '[*] Pattern Hash   : %s\n' % hash.upper()
	# make it as fast as possible
	# pattern -> 1234 -> 01020304 -> \x01\x02\x03\x04 then sha1 hash
	# get all permutations
	for i in range(4, 10):

		permutations = itertools.permutations("012345678", i)

	
		perm_list = map(''.join, permutations)

		for j in perm_list:

			sha = _sha.new(j).hexdigest()

			if hash == sha:
				p = hexlify(j)
				pt = ''.join([p[o] for o in range(1,len(p), 2)])
				print '[+] Pattern Length : %s\n' % len(pt)
				print '[+] Pattern \t   : %s\n' % pt
				patt = svg.draw(pt)
				sv = open('%s.svg' % pt ,'wb')
				sv.write(patt)
				sv.close()
				print '[+] Pattern SVG    : %s.svg\n' % pt
				print '[*] Time : %s sec' % round(time.time() - now, 2)
				exit()
		

	print "[-] Pattern not found !"
	

if __name__ == "__main__":

	if len(sys.argv) < 3:
		print ('p-decode.py [-p hash ] or [-f gesture.key ] or [-g pattern ]')

	elif sys.argv[1] == '-f':
		file = open(sys.argv[2],'rb').read()
		hash = hexlify(file) #file.encode('hex') hexlify fast than encode('hex')
		crack(hash)

	elif sys.argv[1] == '-p':
		hash = sys.argv[2]
		hash = hash.lower() if hash.isupper() else hash
		crack(hash)

	elif sys.argv[1] == '-g':
		print logo
		pat = sys.argv[2]
		gt = unhexlify('0'+'0'.join(pat))
		output = open('gesture.key','wb')
		output.write(_sha.new(gt).digest())
		output.close()
		print '[+] Pattern file : gestrue.key'
	else:
		exit()

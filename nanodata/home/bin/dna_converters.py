from collections import Counter
from random import choice
import binascii
import zlib
import bz2
import itertools

def get_binary(data):
	text_bin_array = []
	for letter in data:
		in_bin = bin(ord(letter))
		if in_bin[0] == '0':
			in_bin = in_bin[2:].zfill(8)
		text_bin_array.append(in_bin)
	return text_bin_array

def get_hex(data):
	hexl = binascii.hexlify(data.encode('utf-8'))
	# print(hexl)
	# print(hex(ord(data)))
	return hexl

def gc_calc(text):
	cnt = Counter(text)
	fraction = (cnt['G'] + cnt['C'])/float(len(text))
	return fraction

def utf8len(s):
	return len(str(s).encode('utf-8'))


class Converters(object):
	def __init__(self):
		self.temp = ''

	def _stats(self, input_text, output_text):
		stats = {
			'input_len': len(input_text),
			'output_len': len(output_text),
			'input_bsize': utf8len(input_text),
			'output_bsize': utf8len(output_text)
			}
		return stats

	def binary(self, query):
		output_text = ''
		if not 'value' in query:
			return output_text
		
		input_text = query['value']
		params = query['params']
		in_binary = get_binary(input_text)

		stats = self._stats(input_text, ''.join(in_binary))

		result = {'output_text': ' '.join(in_binary), 'stats': stats}
		return result

	def hexl(self, query):
		output_text = ''
		if not 'value' in query:
			return output_text
		
		input_text = query['value']
		params = query['params']
		in_hex = get_hex(input_text)
		# print(str(in_hex))
		stats = self._stats(input_text, in_hex)

		result = {'output_text': str(in_hex), 'stats': stats}
		return result

	def church(self, query):
		input_text = query['value']
		params = query['params']
		in_binary = get_binary(input_text)

		bag0=['A','C']
		bag1=['T','G']
		def a_or_c():
			return choice(bag0)
		def t_or_g():
			return choice(bag1)

		
		in_dna = []
		for b_letter in in_binary:
			temp = ''
			for val in b_letter:
				if int(val) == 0:
					temp+=a_or_c()
				else:
					temp+=t_or_g()
			in_dna.append(temp)
		
		dna = ' '.join(in_dna)


		stats = self._stats(input_text, ''.join(in_dna))

		result = {'output_text': dna, 'stats': stats}
		return result

	def zlib(self, query):
		input_text = query['value']
		params = query['params']


		compressed_data = zlib.compress(input_text.encode('utf-8'), 5)

		

		# compress = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, 30)   
		# compressed_data = compress.compress(input_text.encode('utf-8'))
		# compressed_data += compress.flush()
		# print(compressed_data)

		# print('Original data: ' +  input_text)  
		# print('Compressed data: ' + binascii.hexlify(compressed_data).encode('utf-8'))  
		# print('Compressed data: ' + str(compressed_data))

		stats = self._stats(input_text, str(compressed_data))

		result = {'output_text': str(compressed_data), 'stats': stats}
		return result

	def bzip(self, query):
		input_text = query['value']
		params = query['params']


		compressed_data = bz2.compress(input_text.encode('utf-8'))

		# compress = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, 30)   
		# compressed_data = compress.compress(input_text.encode('utf-8'))
		# compressed_data += compress.flush()
		# print(compressed_data)

		# print('Original data: ' +  input_text)  
		# print('Compressed data: ' + binascii.hexlify(compressed_data).encode('utf-8'))  
		# print('Compressed data: ' + str(compressed_data))

		stats = self._stats(input_text, str(compressed_data))

		result = {'output_text': str(compressed_data), 'stats': stats}
		return result



	def home(self, query):
		input_text = query['value']
		params = query['params']

		# print(len(t))
		b = Counter(input_text)
		# print(b)
		it = list(itertools.product(['A','T','C','G'], repeat =4))
		# print(it, len(it), len(b))
		t = {i:''.join(j) for i, j in zip(b, it)}
		# print(t)

		dna=''
		for letter in input_text:
			print(t[letter])
			dna+=t[letter]

		stats = self._stats(input_text, str(dna))

		result = {'output_text': str(dna), 'stats': stats}
		return result


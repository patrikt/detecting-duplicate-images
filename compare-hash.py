#!/usr/bin/python

import hashlib 
import os

PATH = "Photos/"
hash_list = []
file_list = []

for dirname, dirnames, filenames in os.walk(PATH):
    for filename in filenames:
        #print os.path.join(dirname, filename)
        file_path = os.path.join(dirname, filename)
        image_file = open(file_path).read()
        hash_list.append(hashlib.md5(image_file).hexdigest())
        file_list.append(file_path)

N = len(hash_list)
remove_files = []

for (i,entry) in enumerate(hash_list):
	for j in range(i+1,N):
		#print i,j
		if hash_list[i] == hash_list[j]:
			print file_list[i], file_list[j]
			remove_files.append(file_list[j])

for filename in remove_files:
    os.remove(filename)


import sagefs
import sys

fs = None

def quick_hash(s):
	sum = 0
	for c in s: sum += ord(c)
	return sum

def choose_fs_with_hash(s):
	return fs.sites[quick_hash(s) % len(fs.sites)]

def parse_path(path):
	try:
		location, resource = fs.split_location_from_path(path)
		if location in fs.sites: return path
	except sagefs.SageFSInvalidPathException: print 'excepted'
	location = choose_fs_with_hash(path)
	if path[0] is not '/': path = '%s%s' % ('/', path) 
	path = '/%s%s' % (location, path)
	return path

def read(path, create=False):
	path = parse_path(path)
	try: 
		f = fs.open(path, create=create)
		print f.read()
		f.close()
	except sagefs.SageFSFileNotFoundException, e:
		print 'File Not Found'


def write(path, data, create=False, append=True):
	path = parse_path(path)
	try:
		f = fs.open(path, create=create)
		if append: f.seek(2) # 2 is seek end
		# dont sync on write as we will sync on close
		f.write(data, sync=False)
		f.close()
	except sagefs.SageFSFileNotFoundException, e:
		print 'File Not Found'


if __name__ == "__main__":
	fs = sagefs.SageFS('savant', 'savant', 'savant')
	write('/savi/hello.txt', 'hi andi!', True)
	read('/savi/hello.txt', True)
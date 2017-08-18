import funpod
fcp = funpod.FunPodConnector()

def list_yield(f):
	num = int(f.read()); print num
	for i in xrange(num):
		print i; yield i

fcp.handle_file(list_yield)

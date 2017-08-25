from mlpods import funpod
import cPickle


def list_yield(f):
	num = int(f.read()); print num
	for i in xrange(num):
		print i; yield cPickle.dumps(i)


pod = funpod.FunPod('test_pod')
pod.handle_file(list_yield)

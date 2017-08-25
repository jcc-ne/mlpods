# coding: utf-8

from mlpods import funpod
import tempfile

f = tempfile.TemporaryFile()
f.write('10')
f.seek(0)

pod = funpod.FunPod('test_pod')
fcp = pod.connector
g = fcp.client_generator(fileobj=f, start_pod=True)

while True:
    try:
        print g.next()
    except StopIteration:
        print "list ends"
        break

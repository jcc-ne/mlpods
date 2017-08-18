# coding: utf-8

import funpod
import tempfile

f = tempfile.TemporaryFile()
f.write('10')
f.seek(0)

fcp = funpod.FunPodConnector()
g = fcp.client_generator(fileobj=f)

g.next()
g.next()
g.next()
g.next()
g.next()
g.next()
g.next()
g.next()
g.next()
g.next()
g.next()

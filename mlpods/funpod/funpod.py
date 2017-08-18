import socket
import json
import cPickle


class FunPodConnector(object):

    def __init__(self, ip='0.0.0.0', port=9998):
        self.ip = ip
        self.port = port


    def handle(self, func):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(1)

        conn, addr = self.sock.accept()
        print('handle request received')
        try:
            data = True
            buf = ''
            while data:
                data = conn.recv(4096)
                buf += data

            # echo back
            conn.sendall(buf)
            conn.shutdown(socket.SHUT_WR)

        except Exception as e:
            print e

        finally:
            conn.close()

        kwargs = json.loads(buf)
        gen = func(**kwargs)
        for i in gen:
            try:
                conn, addr = self.sock.accept()
                conn.send(str(i))
                conn.shutdown(socket.SHUT_WR)
            finally:
                conn.close()

        try:
            conn, addr = self.sock.accept()
            conn.send('EOF')
            conn.shutdown(socket.SHUT_WR)
        finally:
            conn.close()
        #  n = gen.next()
        #  while n:
        #      print n
        #      self.send(cPickle.dumps(n))
        #      n = gen.next()

    def send(self, data_send):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.ip, self.port))
            #  self.sock.sendall(json.dumps(data_send).encode('utf-8'))
            self.sock.sendall(data_send)
            self.sock.shutdown(socket.SHUT_WR)
            buf = ''
            data = True
            while data:
                data = self.sock.recv(2048)
                buf += data
                #  return json.loads(unicode(buf, 'utf-8'))
        finally:
            self.sock.close()

    def recv(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.ip, self.port))
            #  self.sock.sendall(json.dumps(data_send).encode('utf-8'))

            buf = ''
            data = True
            while data:
                data = self.sock.recv(2048)
                buf += data
            return buf
                #  return json.loads(unicode(buf, 'utf-8'))
        finally:
            self.sock.close()

    def serve_generator(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(1)

        while True:
            conn, addr = self.sock.accept()
            print('client connected')
            try:
                data = True
                buf = ''
                while data:
                    data = conn.recv(4096)
                    buf += data

                # echo back
                conn.sendall(buf)
                conn.shutdown(socket.SHUT_WR)

                #  return json.loads(unicode(buf, 'utf-8'))
                if buf == u'EOF':
                    return
                yield buf

            finally:
                conn.close()

    def client_generator(self, **kwargs):
        self.send(json.dumps(kwargs))
        while True:
            recv = self.recv()
            if recv == 'EOF':
                break
            yield recv


def main_test():
    def makelist(n):
        for i in xrange(int(n)):
            yield i

    connect = FunPodConnector()
    connect.handle(makelist)


if __name__ == '__main__':
    main_test()

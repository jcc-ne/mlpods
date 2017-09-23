import funpod
import cPickle


def test_handler(filepath):
    """
        return content of filepath
    """
    with open(filepath, 'r') as f:
        r = 1
        while r:
            r = f.readline()
            yield cPickle.dumps(r)


pod = funpod.FunPod('test_handle')  # placeholder
pod.handle(test_handler)

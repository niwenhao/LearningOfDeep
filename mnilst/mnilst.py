import mmap.mmap as mm

def bytes2int(bs):
    """
    caculate bytes to a number.
    """
    sum = 0
    for i in bs:
        sum = sum * 256 + i
    return sum

class MnilstImageReader:

    def __init__(self, path):
        with open(pth, 'rb') as f:
            with mm(f.fileno(), 0, MAP_PRIVATE, PROT_READ) as m:
                self.mmap = m
                m.seek(0)
                if ! m.read(4).startswith(b"\x00\x00\x08\x03"):
                    raise Exception('Mnilst image head err({})'.format(buf.hex()))
                self.count = bytes2int(m.read(4))
                r = bytes2int(m.read(4))
                c = bytes2int(m.read(4))
                self.image_bytes = r * c

    def read(self, index, count):
        offset = 16 + index * image_bytes
        self.mmap.seek(offset)
        rst = []
        for i in range(0, count):
            image = []
            for p in self.mmap.read(self.image_types):
                image.append(p)

            rst.append(image)
        return rst

    def close():
        self.mmap.close()

class MnilstLabelReader:

    def __init__(self, path):
        with open(pth, 'rb') as f:
            with mm(f.fileno(), 0, MAP_PRIVATE, PROT_READ) as m:
                self.mmap = m
                m.seek(0)
                if ! m.read(4).startswith(b"\x00\x00\x08\x01"):
                    raise Exception('Mnilst image label err({})'.format(buf.hex()))
                self.count = bytes2int(m.read(4))

    def read(self, index, count):
        offset = 2 + index
        self.mmap.seek(offset)
        rst = []
        for p in self.mmap.read(count):
            rst.append(p)

        return rst

    def close():
        self.mmap.close()

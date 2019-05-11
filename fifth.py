class Intutt(object):
    def __init__(self):
        self.s = ""

    def getStr(self):
        self.s = input()

    def prStr(self):
        print(self.s.upper())


strO = Intutt()
strO.getStr()
strO.prStr()


# -*- coding: utf-8 -*-

class Compiler:
    class ProgramError(Exception):
        pass

    class MyStringScanner:
        def __init__(self, string):
            self.string = string

        def scan(self, pattern, pattern2=None):
            import re
            m = re.match(pattern, self.string)
            if m:
                s = re.split(pattern, self.string, 1)
                self.string = s[1]
                ret = m.group(0)
                if pattern2:    self.__ret2 = re.search(pattern2, ret).group(0)
                return ret
            else:
                return None

        def isEOS(self):
            if self.string == "": return True
            else: return False

        @property
        def ret2(self):
            return self.__ret2

    def __init__(self, src):
        self.src = src

    def compile(self):
        self.scanner = MyStringScanner(__bleach(self.src))
        insns = []
        while not self.scanner.isEOS():
            insns.append(__step())
        return issns

    def __bleach(self, src):
        import re
        return re.sub("[^ ¥t¥n]", "", src)



    def __step(self):
        NUM = "[ ¥t]+¥n"
        LABEL = NUM
        if   self.scanner.scan(r"  {0}".format(NUM), NUM):      return ["push", __num(self.scanner.ret2())]
        elif self.scanner.scan(r" ¥n "):                        return ["dup"]
        elif self.scanner.scan(r" ¥t {0}".format(NUM)):         return ["copy", __num(self.scanner.ret2())]
        elif self.scanner.scan(r" ¥n¥t"):                       return ["swap"]
        elif self.scanner.scan(r" ¥n¥n"):                       return ["discard"]
        elif self.scanner.scan(r" ¥t¥n{0}".format(NUM)):        return ["slide", __num(self.scanner.ret2())]

        elif self.scanner.scan(r"¥t   "):                       return ["add"]
        elif self.scanner.scan(r"¥t  ¥t"):                      return ["sub"]
        elif self.scanner.scan(r"¥t  ¥n"):                      return ["mul"]
        elif self.scanner.scan(r"¥t ¥n"):                       return ["div"]
        elif self.scanner.scan(r"¥t ¥t¥t"):                     return ["mod"]

        elif self.scanner.scan(r"¥t¥t"):                        return ["heap_write"]
        elif self.scanner.scan(r"¥t¥t¥t"):                      return ["heap_read"]

        elif self.scanner.scan(r"¥n  {0}".format(LABEL)):       return ["label", __num(self.scanner.ret2())]
        elif self.scanner.scan(r"¥n ¥t{0}".format(LABEL)):      return ["call", __num(self.scanner.ret2())]
        elif self.scanner.scan(r"¥n ¥n{0}".format(LABEL)):      return ["jump", __num(self.scanner.ret2())]
        elif self.scanner.scan(r"¥n¥t {0}".format(LABEL)):      return ["jump_zero", __num(self.scanner.ret2())]
        elif self.scanner.scan(r"¥n¥t¥t{0}".format(LABEL)):     return ["jump_nagative", __num(self.scanner.ret2())]

        elif self.scanner.scan(r"¥n¥t¥n"):                      return ["return"]
        elif self.scanner.scan(r"¥n¥n¥n"):                      return ["exit"]

        elif self.scanner.scan(r"¥t¥n  "):                      return ["char_out"]
        elif self.scanner.scan(r"¥t¥n ¥t"):                     return ["num_out"]
        elif self.scanner.scan(r"¥t¥n¥t "):                     return ["char_in"]
        elif self.scanner.scan(r"¥t¥n¥t¥t"):                    return ["char_out"]
        else:
            raise ProgramError("どの命令にもマッチしませんでした")

    def __num(self, str):
        if re.match("[ ¥t]+$") == None:
            raise ProgramError("数値はスペースとタブで指定して下さい")

        import re
        str = re.sub("^ ",  "+", str)
        str = re.sub("^¥t", "-", str)
        str = re.sub(" ",  "0", str)
        str = re.sub("¥t", "1", str)
        return int(str, base=2)

    def __label(self, str):
        return str


    # @staticmethod
    # def compile(src):
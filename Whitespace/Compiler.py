# -*- coding: utf-8 -*-

class Compiler:
    class ProgramError(Exception):
        pass

    class MyStringScanner:
        def __init__(self, string):
            self.string = string
            self.__ret2 = ""

        def scan(self, pattern, pattern2=None):
            import re
            m = re.match(pattern, self.string)
            if m:
                s = re.split(pattern, self.string, 1)
                self.string = s[1]
                ret = m.group(0)
                if pattern2:
                    self.__ret2 = re.search(pattern2, ret).group(0)
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
        self.scanner = None

    def compile(self):
        self.scanner = self.MyStringScanner(self.__bleach(self.src))
        insns = []
        while not self.scanner.isEOS():
            insns.append(self.__step())
        return insns

    def __bleach(self, src):
        import re
        return re.sub("[^ ¥t¥n]", "", src)

    def __step(self):
        NUM = "[ ¥t]+¥n"
        NUM_SUB = "( |¥t)+¥n"
        LABEL = NUM
        LABEL_SUB = NUM_SUB
        if   self.scanner.scan(r"  {0}".format(NUM), NUM_SUB):      return ["push", self.__num(self.scanner.ret2)]
        elif self.scanner.scan(r" ¥n "):                            return ["dup"]
        elif self.scanner.scan(r" ¥t {0}".format(NUM), NUM_SUB):    return ["copy", self.__num(self.scanner.ret2)]
        elif self.scanner.scan(r" ¥n¥t"):                           return ["swap"]
        elif self.scanner.scan(r" ¥n¥n"):                           return ["discard"]
        elif self.scanner.scan(r" ¥t¥n{0}".format(NUM), NUM_SUB):   return ["slide", self.__num(self.scanner.ret2)]

        elif self.scanner.scan(r"¥t   "):                           return ["add"]
        elif self.scanner.scan(r"¥t  ¥t"):                          return ["sub"]
        elif self.scanner.scan(r"¥t  ¥n"):                          return ["mul"]
        elif self.scanner.scan(r"¥t ¥n"):                           return ["div"]
        elif self.scanner.scan(r"¥t ¥t¥t"):                         return ["mod"]

        elif self.scanner.scan(r"¥t¥t"):                            return ["heap_write"]
        elif self.scanner.scan(r"¥t¥t¥t"):                          return ["heap_read"]

        elif self.scanner.scan(r"¥n  {0}".format(LABEL), LABEL_SUB):       return ["label", self.__num(self.scanner.ret2)]
        elif self.scanner.scan(r"¥n ¥t{0}".format(LABEL), LABEL_SUB):      return ["call", self.__num(self.scanner.ret2)]
        elif self.scanner.scan(r"¥n ¥n{0}".format(LABEL), LABEL_SUB):      return ["jump", self.__num(self.scanner.ret2)]
        elif self.scanner.scan(r"¥n¥t {0}".format(LABEL), LABEL_SUB):      return ["jump_zero", self.__num(self.scanner.ret2)]
        elif self.scanner.scan(r"¥n¥t¥t{0}".format(LABEL), LABEL_SUB):     return ["jump_nagative", self.__num(self.scanner.ret2)]

        elif self.scanner.scan(r"¥n¥t¥n"):                          return ["return"]
        elif self.scanner.scan(r"¥n¥n¥n"):                          return ["exit"]

        elif self.scanner.scan(r"¥t¥n  "):                          return ["char_out"]
        elif self.scanner.scan(r"¥t¥n ¥t"):                         return ["num_out"]
        elif self.scanner.scan(r"¥t¥n¥t "):                         return ["char_in"]
        elif self.scanner.scan(r"¥t¥n¥t¥t"):                        return ["char_out"]
        else:
            raise ProgramError("どの命令にもマッチしませんでした")

    def __num(self, str):
        import re
        str = re.sub("¥n", "", str)   # 数値後の改行コードは削除
        if re.match("[ ¥t]+$", str) == None:
            raise ProgramError("数値はスペースとタブで指定して下さい")

        str = re.sub("^ ",  "+", str)
        str = re.sub("^¥t", "-", str)
        str = re.sub(" ",  "0", str)
        str = re.sub("¥t", "1", str)
        return int(str, base=2)

    def __label(self, str):
        return str


    # @staticmethod
    # def compile(src):

if __name__ == '__main__':
    print(Compiler("   ¥t¥n").compile())#¥t¥n ¥t¥n¥n¥n").compile())
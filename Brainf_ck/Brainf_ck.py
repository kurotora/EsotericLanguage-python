# -*- coding: utf-8 -*-

import sys

class Brainf_ck:
    def __init__(self, src):
        self.tokens = src
        self.jumps = self.__analizeJumps(self.tokens)

    def run(self, size=256):
        tape = [0] * size   # 指定サイズに合わせてテープの配列作成
        pc = 0
        cur = 0

        while pc < len(self.tokens):
            token = self.tokens[pc]
            if token == "+":
                tape[cur] += 1
            elif token == "-":
                tape[cur] -= 1
            elif token == ">":
                cur += 1
                if len(self.tokens) <= cur:
                    raise ProgramError("テープ範囲外 : pos = {0}".format(cur))
            elif token == "<":
                cur -= 1
                if cur < 0:
                    raise ProgramError("テープ範囲外 : pos = {0}".format(cur))
            elif token == ".":
                print(chr(tape[cur]))
            elif token == ",":
                input = sys.stdin.readline()
                tape[cur] = ord(input[0])
            elif token == "[":
                if tape[cur] == 0:
                    pc = self.jumps[pc]
            elif token == "]":
                if tape[cur] != 0:
                    pc = self.jumps[pc]

            pc += 1
        print(tape)

    def __analizeJumps(self, tokens):
        jumps = {}
        starts = []

        for i, c in enumerate(tokens):
            if c == "[":
                starts.append(i)
            elif c == "]":
                if len(starts) == 0:
                    raise ProgramError("]の数が多い")
                frm = starts.pop()
                to = i
                jumps[frm] = to
                jumps[to] = frm

        if len(starts) != 0:
            raise ProgramError("[の数が多い")

        return jumps


class ProgramError(Exception):
    pass


if __name__ == "__main__":
    text = ""
    try:
        with open(sys.argv[1]) as f:
            for l in f:
                text += l
    except:
        for l in sys.stdin.readlines():
            text += l
    Brainf_ck(text).run()

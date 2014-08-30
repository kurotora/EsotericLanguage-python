# -*- coding: utf-8 -*-

class Compiler:
    class ProgramError(Exception):
        pass

    def __init__(self, src):
        self.src = src

    def compile(self):
        pass

    # @staticmethod
    # def compile(src):
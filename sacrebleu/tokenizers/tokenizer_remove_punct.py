# -*- coding: utf-8 -*-

import regex as re

from .tokenizer_none import NoneTokenizer


class TokenizerNoPunct(NoneTokenizer):
    def signature(self):
        return 'nopea'

    def __init__(self):
        pass

    def __call__(self, line):
        """Tokenizes an input line to remove all punctuation
        except apostrophes; standard for some (ASR) corpora like Fisher

        :param line: a segment to tokenize
        :return: the tokenized line
        """

        #remove all unicode punctuation except apostrophes
        line = re.sub(r"\p{P}", lambda m: "'" if m.group(0) == "'" else "", line)

        #remove any seq of multiple whitespaces left behind
        line = ' '.join(line.split())
        
        return line

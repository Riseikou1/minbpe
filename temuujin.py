from __future__ import annotations

import collections

import regex

import tiktoken

class SimpleBytePairEncoding:
    def __init__(self,*,part_str,mergeable_ranks):
        self.pat_str = part_str
        self.mergeable_ranks = mergeable_ranks
        self._decoder = {token : token_bytes for token_bytes,token in mergeable_ranks.items()}
        self._pat = regex.compile(part_str)


    def encode(self,text,visualise):
        words = self._pat.findall(text)
        tokens = {}
        for word in words :
            word_bytes = word.encode("utf-8")
            word_tokens = bpe_encode(self.mergeable_ranks,word_bytes,visualise=visualise)
            tokens.extend(word_tokens)
        return tokens

    def decode_bytes(self,tokens : list[int]) -> bytes :
        return b"".join(self._decoder[token] for token in tokens)

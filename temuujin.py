from __future__ import annotations

import collections

import regex

import tiktoken


def __init__(self,*,part_str,mergeable_ranks):
    self.pat_str = part_str
    self.mergeable_ranks = mergeable_ranks
    self._decoder = {token : token_bytes for token_bytes,token in mergeable_ranks.items()}
    
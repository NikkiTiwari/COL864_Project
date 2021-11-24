#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TermVocab:
    def __init__(self):
        self.track2index = {}
        self.index2track = {}
        self.track2count = {}
        self.vocab_length = 0
    
    def add_track(self, track):
        if track not in self.track2count:
            self.track2index[track] = self.vocab_length
            self.track2count[track] = 1
            self.index2track[self.vocab_length] = track
            self.vocab_length += 1
        else:
            self.track2count[track] += 1
        return
    
    def to_track(self, index):
        if index >= self.vocab_length:
            print('vocab index out of bound')
            raise Exception('Vocab index out of bound')
        return self.index2track[index]
    
    def to_index(self, track):
        if track not in self.track2index.keys():
           #print('Track not found in Vocab')
           return -1
        return self.track2index[track]
    
    def get_count(self, track):
        return self.track2count[track]


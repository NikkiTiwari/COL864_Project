import numpy as np
import os
import json
import pandas as pd
import time
from tqdm import tqdm
import gc
import mmap
from scipy import spatial
import heapq

from Vocab_class import TermVocab

def create_vocab(coll_dir, TVocab :type(TermVocab()) = TermVocab(), validation_pl_upto = 200):
    limit_file_read_to = 5
    idf = {}
    s = 0.1
    print('Creating Track Vocabulary')
    file_count = 0
    filenames = ['mpd.slice.102000-102999.json',
                 'mpd.slice.103000-103999.json',
                 'mpd.slice.104000-104999.json',
                 'mpd.slice.101000-101999.json',
                 'mpd.slice.10000-10999.json']
    #for filename in sorted(os.listdir(coll_dir)):
    for filename in filenames:
        file_count += 1
        #print('For File:', filename)
        with open(os.path.join(coll_dir, filename), 'r') as f:
            mm = mmap.mmap(f.fileno(),length = 0, access = mmap.ACCESS_READ)
            playlists = json.load(mm)['playlists']
            # print('total playlists:', len(playlists))
            for playlist in playlists[validation_pl_upto:]:
                tracks = playlist['tracks']
                # print('\tTotal Tracks:', len(tracks))
                for track in tracks[:]:
                    track_uri = track['track_uri']
                    if track_uri not in idf:
                        idf[track_uri] = 1/s
                    idf[track_uri] = 1/((1/idf[track_uri]) + 1)
                    TVocab.add_track(track_uri)
                    # print('\tPOS :',track['pos'])
                    # print('\tName: ',track['track_name'])
                    # print('\tURI : ',track['track_uri'])
            mm.close()
        if file_count >= limit_file_read_to:
            break
    return TVocab, idf

# collection_dir = '../spotify_million_playlist_dataset/data/'
#collection_dir = '/media/harsh/Common/IITD/COL764-IR/Project/spotify_million_playlist_dataset/data/'
#TVocab = create_vocab(collection_dir)
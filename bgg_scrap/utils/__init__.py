import os
import pickle

import tqdm


def merge_cache_files(target='cache'):
    final = []
    objects = set()
    for file in os.listdir("./"):
        if file.endswith(".pickle") and not file.startswith(target):
            l = pickle.load(open(file, 'rb'))
            pb = tqdm.tqdm(total=len(l))
            for item in l:
                pb.update(1)
                if 'item' in item[0].keys() and item[0]['item']['itemstate'] == 'approved' and item[0]['item'][
                    'objectid'] not in objects:
                    final.append(item)
                    objects.add(item[0]['item']['objectid'])

    def ckey(item):
        return item[0]['item']['objectid']

    final.sort(key=ckey)

    pickle.dump(final, open(target + '.pickle', 'wb'))

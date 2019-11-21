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


def delete_inaccepted(session, basis='rejected', fr=True):
    if fr:
        from bgg_scrap.models.db_fr import Game, NbPlayers
    else:
        from bgg_scrap.models.db_en import Game, NbPlayers
    final = pickle.load(open(basis + '.pickle', 'rb'))
    pb = tqdm.tqdm(total=len(final))

    for data, stats in final:
        id = data['item']['objectid']
        geekitem = session.query(Game).filter(Game.id == int(id))
        if geekitem.count() == 1:
            g = geekitem.one()
            nbp = session.query(NbPlayers).filter(NbPlayers.game_id == int(id)).all()
            for x in nbp:
                session.delete(x)
            session.delete(g)
        pb.update()

    session.commit()

import argparse
import json
import multiprocessing as mp
import urllib.request
from json import JSONDecodeError
from queue import Queue

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


def fetch_bgg(game_id):
    game_stats = {}
    url = 'https://api.geekdo.com/api/geekitems?objectid=' + str(game_id) + '&objecttype=thing'
    with urllib.request.urlopen(url) as u:
        try:
            game_data = json.loads(u.read().decode())
        except JSONDecodeError:
            return {'game': game_id}, {}
    if int(game_data['item']['objectid']) != int(game_id) or game_data['item']['subtype'] == 'boardgameaccessory':
        game_data = {}
    else:
        url = 'https://api.geekdo.com/api/dynamicinfo?objectid=' + str(game_id) + '&objecttype=thing'
        try:
            with urllib.request.urlopen(url) as u:
                game_stats = json.loads(u.read().decode())
        except urllib.request.HTTPError:
            pass
        except JSONDecodeError:
            return {'game': game_id}, {}
    return game_data, game_stats


def languagedependence(data):
    try:
        l = session.query(Verbosity).filter(Verbosity.text == data).one()
    except NoResultFound:
        l = Verbosity(text=data)
        session.add(l)
    return l


def parse_person(person):
    try:
        a = session.query(Person).filter(Person.id == person['objectid']).one()
    except NoResultFound:
        a = Person(id=person['objectid'], name=person['name'])
        session.add(a)
    return a


def parse_company(publisher):
    try:
        c = session.query(Company).filter(Company.id == publisher['objectid']).one()
    except NoResultFound:
        c = Company(id=publisher['objectid'], name=publisher['name'])
        url = 'https://api.geekdo.com/api/geekitems?objectid=' + str(publisher['objectid']) + '&objecttype=company'
        with urllib.request.urlopen(url) as u:
            company_data = json.loads(u.read().decode())
        if int(company_data['item']['objectid']) != int(publisher['objectid']):
            website = None
        else:
            website = company_data['item']['website']['url'] if company_data['item']['website']['url'] else None
        c.website = website
        session.add(c)
    return c


def parse_property(property, type):
    if type == 'category':
        try:
            p = session.query(Category).filter(Category.id == property['objectid']).one()
        except NoResultFound:
            p = Category(id=property['objectid'], name=property['name'])
            session.add(p)
        return p
    elif type == 'mechanic':
        try:
            p = session.query(Mechanic).filter(Mechanic.id == property['objectid']).one()
        except NoResultFound:
            p = Mechanic(id=property['objectid'], name=property['name'])
            session.add(p)
        return p
    return None


def parse_label(label, subtype):
    if subtype == 'family':
        try:
            f = session.query(Family).filter(Family.id == label['objectid']).one()
        except NoResultFound:
            f = Family(id=label['objectid'], name=label['name'])
            url = 'https://api.geekdo.com/api/geekitems?objectid=' + str(label['objectid']) + '&objecttype=family'
            with urllib.request.urlopen(url) as u:
                family_data = json.loads(u.read().decode())
            if int(family_data['item']['objectid']) != int(label['objectid']):
                description = None
            else:
                description = family_data['item']['description']
            f.description = description
            session.add(f)
        return f
    elif subtype == 'subdomain':
        try:
            f = session.query(SubDomain).filter(SubDomain.id == label['objectid']).one()
        except NoResultFound:
            f = SubDomain(id=label['objectid'], name=label['name'])
            session.add(f)
        return f
    return None


def parse_game_data(game_data, game_stats):
    if 'item' not in game_data.keys():
        raise Exception()
    item = game_data['item']
    add = False
    # print(item.keys())

    # for key in item.keys():
    #    print(key, item[key])

    try:
        b = session.query(Game).filter(Game.id == item['objectid']).one()
    except NoResultFound:
        add = True
        b = Game(id=item['objectid'], name=item['name'])
    b.type = item['subtype']
    if b.type in ['videogame']:
        if add:
            session.add(b)
        else:
            session.merge(b)
        session.commit()
        return None, b
    b.yearpublished = item['yearpublished']

    b.minplayers = item['minplayers']
    b.maxplayers = item['maxplayers']
    b.minplaytime = item['minplaytime']
    b.maxplaytime = item['maxplaytime']
    b.minage = item['minage']

    if 'item' in game_stats.keys():
        stats = game_stats['item']
        # for k in stats:
        #    print(k, stats[k])
        for rankinfo in stats['rankinfo']:
            if rankinfo['veryshortprettyname'] == 'Overall':
                b.rank = rankinfo['rank']
        s = stats['stats']
        b.average_rating = s['average']
        b.bayes_average_rating = s['baverage']
        p = stats['polls']
        if len(p['userplayers']['best']) > 1:
            print(b.id, 'has more than one best')
        elif len(p['userplayers']['best']) == 1:
            b.best_minplayers = p['userplayers']['best'][0]['min']
            b.best_maxplayers = p['userplayers']['best'][0]['max']
        if len(p['userplayers']['recommended']) > 1:
            print(b.id, 'has more than one recommended')
        elif len(p['userplayers']['recommended']) == 1:
            b.recommended_minplayers = p['userplayers']['recommended'][0]['min']
            b.recommended_maxplayers = p['userplayers']['recommended'][0]['max']
        b.recommended_age = p['playerage']

        b.languagedependency = languagedependence(p['languagedependence'])

    links = item['links']

    for artist in links['boardgameartist']:
        b.artists.append(parse_person(artist))

    for designer in links['boardgamedesigner']:
        b.designers.append(parse_person(designer))

    for publisher in links['boardgamepublisher']:
        b.publishers.append(parse_company(publisher))

    for category in links['boardgamecategory']:
        b.categories.append(parse_property(category, 'category'))

    for mechanic in links['boardgamemechanic']:
        b.mechanics.append(parse_property(mechanic, 'mechanic'))

    for label in links['boardgamefamily']:
        b.families.append(parse_label(label, 'family'))

    for label in links['boardgamesubdomain']:
        b.subdomains.append(parse_label(label, 'subdomain'))

    # for link in links:
    #     print(link, links[link])

    pf_flag = False
    postfix = {'contains': [], 'reimplements': [], 'expandsboardgame': []}

    if len(links['contains']) > 0:
        [postfix['contains'].append(o['objectid']) for o in links['contains']]
        pf_flag = True

    if len(links['reimplements']) > 0:
        [postfix['reimplements'].append(o['objectid']) for o in links['reimplements']]
        pf_flag = True

    if len(links['expandsboardgame']) > 0:
        [postfix['expandsboardgame'].append(o['objectid']) for o in links['expandsboardgame']]
        pf_flag = True

    # TODO: boardgameversion

    # TODO: better recommended/best max/min players

    if add:
        session.add(b)
    else:
        session.merge(b)
    session.commit()

    if not pf_flag:
        postfix = None
    return postfix, b


def db_fetch(entry):
    try:
        return session.query(Game).filter(Game.id == entry).one()
    except NoResultFound:
        return None


def process_fetch(queue):
    thing = queue.get()
    if 'games' in thing.keys():
        fetched = [x[0] for x in session.query(Game.id).all()]
        with mp.Pool(processes=4) as p:
            results = p.map(fetch_bgg, [i for i in thing['games'] if i not in fetched])
        final = [r for r in results if len(r[0]) > 0]
        for row in final:
            game_data, game_stats = row
            if 'game' in game_data.keys():
                queue.put(game_data)
            else:
                try:
                    postfix, game = parse_game_data(game_data, game_stats)
                    if postfix is not None:
                        queue.put({'postfix': (game, postfix)})
                except:
                    print(game_data)
                    raise
    elif 'game' in thing.keys():
        game_data, game_stats = fetch_bgg(thing['game'])
        try:
            postfix, game = parse_game_data(game_data, game_stats)
            if postfix is not None:
                queue.put({'postfix': (game, postfix)})
        except:
            raise
    elif 'postfix' in thing.keys():
        g, subgames = thing["postfix"]
        print(g.id, subgames)
        for entry in subgames['contains']:
            game = db_fetch(entry)
            if not game:
                entry_data, entry_stats = fetch_bgg(entry)
                postfix, game = parse_game_data(entry_data, entry_stats)
                if postfix is not None:
                    queue.put({'postfix': (game, postfix)})
            g.contains.append(game)
        for entry in subgames['reimplements']:
            game = db_fetch(entry)
            if not game:
                entry_data, entry_stats = fetch_bgg(entry)
                postfix, game = parse_game_data(entry_data, entry_stats)
                if postfix is not None:
                    queue.put({'postfix': (game, postfix)})
            g.reimplements.append(game)
        for entry in subgames['expandsboardgame']:
            game = db_fetch(entry)
            if not game:
                entry_data, entry_stats = fetch_bgg(entry)
                postfix, game = parse_game_data(entry_data, entry_stats)
                if postfix is not None:
                    queue.put({'postfix': (game, postfix)})
            g.expands.append(game)
        session.merge(g)
        session.commit()
    else:
        print(thing)


def main(arguments):
    queue = Queue()
    if arguments.game_id is not None:
        queue.put({'game': arguments.game_id})
    else:
        queue.put({'games': [i + 1 for i in range(arguments.max_game_id)]})
    while not queue.empty():
        process_fetch(queue)

        #     if arguments.v:
        #         nb_games = session.query(Game).count()
        #         nb_pers = session.query(Person).count()
        #         nb_comp = session.query(Company).count()
        #         print('Stats: ', nb_games, ' games, ', nb_pers, ' persons, ', nb_comp, ' companies')


if __name__ == "__main__":
    # execute only if run as a script
    parser = argparse.ArgumentParser(prog='bgg_scrap')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-m", "--max-game-id", type=int, nargs='?', const=42,
                       help="Parse all the games up to MAX_GAME_ID (~300000)")
    group.add_argument("-i", "--game-id", type=int, nargs='?', const=42,
                       help="Parse only GAME_ID")
    parser.add_argument('-fr', action="store_true",
                        help="Use French DB names")
    parser.add_argument('-d', action="store_true",
                        help="Debug")
    parser.add_argument('-v', action="store_true",
                        help="Verbose")
    # Actual max right now : 300000
    args = parser.parse_args()
    if args.fr:
        from db_fr import Base, Game, Verbosity, Person, Company, Category, Mechanic, Family, SubDomain

        engine = create_engine('sqlite:///bgg_fr.sqlite', echo=False)
    else:
        from db_en import Base, Game, Verbosity, Person, Company, Category, Mechanic, Family, SubDomain

        engine = create_engine('sqlite:///bgg_en.sqlite', echo=False)
    if args.d:
        engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    lock = mp.Lock()

    main(args)

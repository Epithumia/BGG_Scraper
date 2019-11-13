import argparse
import json
import logging
import multiprocessing as mp
from datetime import datetime
from json import JSONDecodeError
from queue import Queue

import urllib3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from urllib3 import Retry


def fetch_bgg(game_id):
    game_stats = {}
    url = 'https://api.geekdo.com/api/geekitems?objectid=' + str(game_id) + '&objecttype=thing'
    u = http.request('GET', url)
    try:
        game_data = json.loads(u.data.decode())
    except JSONDecodeError:
        return {'game': game_id}, {}
    if int(game_data['item']['objectid']) != int(game_id):
        game_data = {}
    else:
        url = 'https://api.geekdo.com/api/dynamicinfo?objectid=' + str(game_id) + '&objecttype=thing'
        try:
            u = http.request('GET', url)
            game_stats = json.loads(u.data.decode())
        except JSONDecodeError:
            return {'game': game_id}, {}
    return game_data, game_stats


def fetch_version(version_id):
    game_stats = {}
    url = 'https://api.geekdo.com/api/geekitems?objectid=' + str(version_id) + '&objecttype=version'

    u = http.request('GET', url)
    try:
        game_data = json.loads(u.data.decode())
    except JSONDecodeError:
        return {'game': version_id}, {}

    if int(game_data['item']['objectid']) != int(version_id):
        game_data = {}

    return game_data, game_stats


def languagedependence(data):
    logger.debug(" --> Language dependence")
    try:
        ld = session.query(Verbosity).filter(Verbosity.text == data).one()
    except NoResultFound:
        ld = Verbosity(text=data)
        session.add(ld)
    return ld


def parse_person(person):
    logger.debug(" --> Person : " + person['name'])
    try:
        a = session.query(Person).filter(Person.id == person['objectid']).one()
        logger.debug("     --> Exists")
    except NoResultFound:
        a = Person(id=person['objectid'], name=person['name'])
        session.add(a)
        logger.debug("     --> Added")
    return a


def parse_company(publisher):
    logger.debug(" --> Company : " + publisher['name'])
    try:
        c = session.query(Company).filter(Company.id == publisher['objectid']).one()
        logger.debug("     --> Exists")
    except NoResultFound:
        c = Company(id=publisher['objectid'], name=publisher['name'])
        url = 'https://api.geekdo.com/api/geekitems?objectid=' + str(publisher['objectid']) + '&objecttype=company'
        u = http.request('GET', url)
        company_data = json.loads(u.data.decode())
        if int(company_data['item']['objectid']) != int(publisher['objectid']):
            website = None
        else:
            website = company_data['item']['website']['url'] if company_data['item']['website']['url'] else None
        c.website = website
        session.add(c)
        logger.debug("     --> Added")
    return c


def parse_property(bgg_property, property_type):
    logger.debug(" --> Property : " + property_type)
    if property_type == 'category':
        try:
            p = session.query(Category).filter(Category.id == bgg_property['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            p = Category(id=bgg_property['objectid'], name=bgg_property['name'])
            session.add(p)
            logger.debug("     --> Added")
        return p
    elif property_type == 'mechanic':
        try:
            p = session.query(Mechanic).filter(Mechanic.id == bgg_property['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            p = Mechanic(id=bgg_property['objectid'], name=bgg_property['name'])
            session.add(p)
            logger.debug("     --> Added")
        return p
    elif property_type == 'videogamegenre':
        try:
            p = session.query(VideoGameGenre).filter(VideoGameGenre.id == bgg_property['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            p = VideoGameGenre(id=bgg_property['objectid'], name=bgg_property['name'])
            session.add(p)
            logger.debug("     --> Added")
        return p
    elif property_type == 'videogametheme':
        try:
            p = session.query(VideoGameTheme).filter(VideoGameTheme.id == bgg_property['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            p = VideoGameTheme(id=bgg_property['objectid'], name=bgg_property['name'])
            session.add(p)
            logger.debug("     --> Added")
        return p
    elif property_type == 'videogamemode':
        try:
            p = session.query(VideoGameMode).filter(VideoGameMode.id == bgg_property['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            p = VideoGameMode(id=bgg_property['objectid'], name=bgg_property['name'])
            session.add(p)
            logger.debug("     --> Added")
        return p
    elif property_type == 'language':
        try:
            p = session.query(Language).filter(Language.id == bgg_property['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            p = Language(id=bgg_property['objectid'], name=bgg_property['name'])
            session.add(p)
            logger.debug("     --> Added")
        return p
    else:
        logger.error('Unknown:' + bgg_property)
        raise Exception()


def parse_family(label, subtype):
    logger.debug(" --> Family : " + subtype)
    if subtype == 'boardgamefamily':
        try:
            f = session.query(Family).filter(Family.id == label['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            f = BoardGameFamily(id=label['objectid'], name=label['name'])
            url = 'https://api.geekdo.com/api/geekitems?objectid=' + str(label['objectid']) + '&objecttype=family'
            u = http.request('GET', url)
            family_data = json.loads(u.data.decode())
            if int(family_data['item']['objectid']) != int(label['objectid']):
                description = None
            else:
                description = family_data['item']['description']
            f.description = description
            session.add(f)
            logger.debug("     --> Added")
        return f
    elif subtype == 'boardgamesubdomain':
        try:
            f = session.query(BoardGameSubdomain).filter(BoardGameSubdomain.id == label['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            f = BoardGameSubdomain(id=label['objectid'], name=label['name'])
            session.add(f)
            logger.debug("     --> Added")
        return f
    elif subtype == 'videogamefranchise':
        try:
            f = session.query(VGFranchise).filter(VGFranchise.id == label['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            f = VGFranchise(id=label['objectid'], name=label['name'])
            logger.debug("     --> Added")
            session.add(f)
        return f
    elif subtype == 'videogameplatform':
        try:
            f = session.query(VGPlatforms).filter(VGPlatforms.id == label['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            f = VGPlatforms(id=label['objectid'], name=label['name'])
            logger.debug("     --> Added")
            session.add(f)
        return f
    elif subtype == 'videogameseries':
        try:
            f = session.query(VGSeries).filter(VGSeries.id == label['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            f = VGSeries(id=label['objectid'], name=label['name'])
            logger.debug("     --> Added")
            session.add(f)
        return f
    elif subtype == 'rpg':
        try:
            f = session.query(RPG).filter(RPG.id == label['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            f = RPG(id=label['objectid'], name=label['name'])
            logger.debug("     --> Added")
            session.add(f)
        return f
    elif subtype == 'rpggenre':
        try:
            f = session.query(RPGGenre).filter(RPGGenre.id == label['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            f = RPGGenre(id=label['objectid'], name=label['name'])
            logger.debug("     --> Added")
            session.add(f)
        return f
    elif subtype == 'rpgsetting':
        try:
            f = session.query(RPGSetting).filter(RPGSetting.id == label['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            f = RPGSetting(id=label['objectid'], name=label['name'])
            logger.debug("     --> Added")
            session.add(f)
        return f
    elif subtype == 'rpgseries':
        try:
            f = session.query(RPGSeries).filter(RPGSeries.id == label['objectid']).one()
            logger.debug("     --> Exists")
        except NoResultFound:
            f = RPGSeries(id=label['objectid'], name=label['name'])
            logger.debug("     --> Added")
            session.add(f)
        return f
    return None


def parse_game_data(game_data, game_stats):
    if 'item' not in game_data.keys():
        raise Exception()
    item = game_data['item']

    if item['subtype'] == 'boardgame' or (item['subtype'] == 'boardgameexpansion' and 'boardgame' in item['subtypes']):
        logger.debug('boardgame')
        return parse_boardgame(item, game_stats)
    elif item['subtype'] == 'boardgameaccessory':
        logger.debug('boardgameaccessory')
        return parse_boardgameaccessory(item, game_stats)
    elif item['subtype'] == 'videogame' or (
            item['subtype'] == 'videogameexpansion' and 'videogame' in item['subtypes']):
        item['subtype'] = 'videogame'
        logger.debug('videogame')
        return parse_videogame(item, game_stats)
    elif item['subtype'] == 'rpgitem':
        logger.debug('rpgitem')
        return parse_roleplayinggame(item, game_stats)
    elif item['subtype'] == 'rpgissue':
        logger.debug('rpgissue')
        return parse_rpgissue(item, game_stats)
    elif item['subtype'] in ['boardgameversion', 'bgaccessoryversion']:
        logger.debug('version')
        return parse_version(item, item['subtype'])
    else:
        logger.warning('Type inconnu : ' + item['subtype'] + ' (item #' + str(item['objectid']) + ')')
        return None, []


def parse_version(item, subtype):
    logger.debug("Parsing version #" + str(item['objectid']))
    add = False
    if subtype == 'boardgameversion':
        try:
            b = session.query(BoardGameVersion).filter(BoardGameVersion.id == item['objectid']).one()
        except NoResultFound:
            add = True
            b = BoardGameVersion(id=item['objectid'], versionname=item['versionname'])
        links = item['links']
        for artist in links['boardgameartist']:
            b.artists.append(parse_person(artist))

        for publisher in links['boardgamepublisher']:
            b.publishers.append(parse_company(publisher))

        for language in links['languages']:
            b.languages.append(parse_property(language, 'language'))

        b.yearpublished = item['yearpublished']
    elif subtype == 'bgaccessoryversion':
        try:
            b = session.query(BoardGameAccessoryVersion).filter(BoardGameAccessoryVersion.id == item['objectid']).one()
        except NoResultFound:
            add = True
            b = BoardGameAccessoryVersion(id=item['objectid'], versionname=item['versionname'])
    else:
        raise NotImplementedError()

    b.linkedname = item['linkedname']

    if add:
        session.add(b)
    else:
        session.merge(b)
    session.commit()

    return None, b


def parse_videogame(item, game_stats):
    logger.debug("Parsing videogame #" + str(item['objectid']))
    add = False
    try:
        b = session.query(VideoGame).filter(VideoGame.id == item['objectid']).one()
    except NoResultFound:
        add = True
        b = VideoGame(id=item['objectid'], name=item['name'])
    b.type = item['subtype']

    dt = datetime.strptime(item['releasedate'], '%Y-%m-%d')
    b.yearpublished = dt.year

    b.minplayers = item['minplayers']
    b.maxplayers = item['maxplayers']

    if 'item' in game_stats.keys():
        stats = game_stats['item']
        for rankinfo in stats['rankinfo']:
            if rankinfo['prettyname'] == 'Video Game Rank':
                b.rank = rankinfo['rank']
        s = stats['stats']
        b.average_rating = s['average']
        b.bayes_average_rating = s['baverage']

    links = item['links']

    for publisher in links['videogamepublisher']:
        b.publishers.append(parse_company(publisher))

    for developer in links['videogamedeveloper']:
        b.developers.append(parse_company(developer))

    for genre in links['videogamegenre']:
        b.genres.append(parse_property(genre, 'videogamegenre'))

    for theme in links['videogametheme']:
        b.themes.append(parse_property(theme, 'videogametheme'))

    for mode in links['videogamemode']:
        b.modes.append(parse_property(mode, 'videogamemode'))

    for franchise in links['videogamefranchise']:
        b.franchises.append(parse_family(franchise, 'videogamefranchise'))

    for platform in links['videogameplatform']:
        b.platforms.append(parse_family(platform, 'videogameplatform'))

    for series in links['videogameseries']:
        b.series.append(parse_family(series, 'videogameseries'))

    pf_flag = False
    postfix = {'contains': [], 'expandsvideogame': []}

    # TODO : testcase with contains
    if len(links['contains']) > 0:
        [postfix['contains'].append(o['objectid']) for o in links['contains']]
        pf_flag = True

    if len(links['expandsvideogame']) > 0:
        [postfix['expandsvideogame'].append(o['objectid']) for o in links['expandsvideogame']]
        pf_flag = True

    if add:
        session.add(b)
    else:
        session.merge(b)
    session.commit()

    if not pf_flag:
        postfix = None
    return postfix, b


def parse_boardgame(item, game_stats):
    logger.debug("Parsing boardgame #" + str(item['objectid']))
    add = False
    try:
        b = session.query(BoardGame).filter(BoardGame.id == item['objectid']).one()
    except NoResultFound:
        add = True
        b = BoardGame(id=item['objectid'], name=item['name'])

    b.yearpublished = item['yearpublished']

    b.minplayers = item['minplayers']
    b.maxplayers = item['maxplayers']
    b.minplaytime = item['minplaytime']
    b.maxplaytime = item['maxplaytime']
    b.minage = item['minage']

    if 'item' in game_stats.keys():
        stats = game_stats['item']
        for rankinfo in stats['rankinfo']:
            if rankinfo['veryshortprettyname'] == 'Overall':
                b.rank = rankinfo['rank']
        s = stats['stats']
        b.average_rating = s['average']
        b.bayes_average_rating = s['baverage']
        p = stats['polls']
        nbp_id = 0
        for oldbest in b.best:
            session.delete(oldbest)
        for best in p['userplayers']['best']:
            b.best.append(Best(id=nbp_id, min=best['min'], max=best['max']))
            nbp_id += 1
        for oldrecommended in b.recommended:
            session.delete(oldrecommended)
        for recommended in p['userplayers']['recommended']:
            b.recommended.append(Recommended(id=nbp_id, min=recommended['min'], max=recommended['max']))
            nbp_id += 1

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
        b.boardgamefamilies.append(parse_family(label, 'boardgamefamily'))

    for label in links['boardgamesubdomain']:
        b.boardgamesubdomains.append(parse_family(label, 'boardgamesubdomain'))

    pf_flag = False
    postfix = {'contains': [], 'reimplements': [], 'expandsboardgame': [], 'boardgameaccessory': [],
               'boardgameversion': []}

    if len(links['contains']) > 0:
        [postfix['contains'].append(o['objectid']) for o in links['contains']]
        pf_flag = True

    if len(links['reimplements']) > 0:
        [postfix['reimplements'].append(o['objectid']) for o in links['reimplements']]
        pf_flag = True

    if len(links['expandsboardgame']) > 0:
        [postfix['expandsboardgame'].append(o['objectid']) for o in links['expandsboardgame']]
        pf_flag = True

    if len(links['boardgameaccessory']) > 0:
        [postfix['boardgameaccessory'].append(o['objectid']) for o in links['boardgameaccessory']]
        pf_flag = True

    if len(links['boardgameversion']) > 0:
        [postfix['boardgameversion'].append(o['objectid']) for o in links['boardgameversion']]
        pf_flag = True

    if add:
        session.add(b)
    else:
        session.merge(b)
    session.commit()

    if not pf_flag:
        postfix = None
    return postfix, b


def parse_rpgissue(item, game_stats):
    logger.debug("Parsing boardgame #" + str(item['objectid']))
    add = False
    try:
        b = session.query(RPGIssue).filter(RPGIssue.id == item['objectid']).one()
    except NoResultFound:
        add = True
        b = RPGIssue(id=item['objectid'], name=item['primaryname']['name'])

    if 'item' in game_stats.keys():
        stats = game_stats['item']
        for rankinfo in stats['rankinfo']:
            if rankinfo['prettyname'] == 'RPG Issue Rank':
                b.rank = rankinfo['rank']
        s = stats['stats']
        b.average_rating = s['average']
        b.bayes_average_rating = s['baverage']

    if add:
        session.add(b)
    else:
        session.merge(b)
    session.commit()

    return None, b


def parse_roleplayinggame(item, game_stats):
    logger.debug("Parsing boardgame #" + str(item['objectid']))
    add = False
    try:
        b = session.query(RolePlayingGame).filter(RolePlayingGame.id == item['objectid']).one()
    except NoResultFound:
        add = True
        b = RolePlayingGame(id=item['objectid'], name=item['name'])

    b.yearpublished = item['yearpublished']

    if 'item' in game_stats.keys():
        stats = game_stats['item']
        for rankinfo in stats['rankinfo']:
            if rankinfo['prettyname'] == 'RPG Item Rank':
                b.rank = rankinfo['rank']
        s = stats['stats']
        b.average_rating = s['average']
        b.bayes_average_rating = s['baverage']

    links = item['links']

    for artist in links['rpgartist']:
        b.artists.append(parse_person(artist))

    for producer in links['rpgproducer']:
        b.producers.append(parse_person(producer))

    for designer in links['rpgdesigner']:
        b.designers.append(parse_person(designer))

    for publisher in links['rpgpublisher']:
        b.publishers.append(parse_company(publisher))

    for category in links['rpgcategory']:
        b.categories.append(parse_property(category, 'category'))

    for mechanic in links['rpgmechanic']:
        b.mechanics.append(parse_property(mechanic, 'mechanic'))

    for label in links['rpgsetting']:
        b.settings.append(parse_family(label, 'rpgsetting'))

    for label in links['rpg']:
        b.rpgs.append(parse_family(label, 'rpg'))

    for label in links['rpgseries']:
        b.series.append(parse_family(label, 'rpgseries'))

    for label in links['rpggenre']:
        b.genres.append(parse_family(label, 'rpggenre'))

    if add:
        session.add(b)
    else:
        session.merge(b)
    session.commit()

    return None, b


def parse_boardgameaccessory(item, game_stats):
    logger.debug("Parsing boardgame accessory #" + str(item['objectid']))
    add = False
    try:
        b = session.query(BoardGameAccessory).filter(BoardGameAccessory.id == item['objectid']).one()
    except NoResultFound:
        add = True
        b = BoardGameAccessory(id=item['objectid'], name=item['name'])
    b.type = item['subtype']

    b.yearpublished = item['yearpublished']

    if 'item' in game_stats.keys():
        stats = game_stats['item']
        for rankinfo in stats['rankinfo']:
            if rankinfo['prettyname'] == 'Accessory Rank':
                b.rank = rankinfo['rank']
        s = stats['stats']
        b.average_rating = s['average']
        b.bayes_average_rating = s['baverage']

    links = item['links']

    for artist in links['boardgameartist']:
        b.artists.append(parse_person(artist))

    for designer in links['boardgamedesigner']:
        b.designers.append(parse_person(designer))

    for publisher in links['boardgamepublisher']:
        b.publishers.append(parse_company(publisher))

    # TODO: testcase with family
    for label in links['bgaccessoryfamily']:
        b.boardgamefamilies.append(parse_family(label, 'bgaccessoryfamily'))

    pf_flag = False
    postfix = {'contains': [], 'reimplements': [], 'expandsboardgame': [], 'boardgameaccessory': [],
               'boardgameversion': [], 'bgaccessoryversion': []}

    if len(links['bgaccessoryversion']) > 0:
        [postfix['bgaccessoryversion'].append(o['objectid']) for o in links['bgaccessoryversion']]
        pf_flag = True

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


def db_fetch_version(entry):
    try:
        return session.query(Version).filter(Version.id == entry).one()
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
        if 'reimplements' not in subgames:
            subgames['reimplements'] = []
        if 'expandsvideogame' not in subgames:
            subgames['expandsvideogame'] = []
        if 'expandsboardgame' not in subgames:
            subgames['expandsboardgame'] = []
        if 'boardgameaccessory' not in subgames:
            subgames['boardgameaccessory'] = []
        if 'boardgameversion' not in subgames:
            subgames['boardgameversion'] = []
        if 'bgaccessoryversion' not in subgames:
            subgames['bgaccessoryversion'] = []
        if verbose:
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
        for entry in subgames['expandsvideogame']:
            game = db_fetch(entry)
            if not game:
                entry_data, entry_stats = fetch_bgg(entry)
                postfix, game = parse_game_data(entry_data, entry_stats)
                if postfix is not None:
                    queue.put({'postfix': (game, postfix)})
            g.expands.append(game)
        for entry in subgames['boardgameaccessory']:
            game = db_fetch(entry)
            if not game:
                entry_data, entry_stats = fetch_bgg(entry)
                postfix, game = parse_game_data(entry_data, entry_stats)
                if postfix is not None:
                    queue.put({'postfix': (game, postfix)})
            g.boardgameaccessories.append(game)
        for entry in subgames['boardgameversion']:
            version = db_fetch_version(entry)
            if not version:
                entry_data, entry_stats = fetch_version(entry)
                _, version = parse_game_data(entry_data, entry_stats)
            g.versions.append(version)
        for entry in subgames['bgaccessoryversion']:
            version = db_fetch_version(entry)
            if not version:
                entry_data, entry_stats = fetch_version(entry)
                _, version = parse_game_data(entry_data, entry_stats)
            g.versions.append(version)
        session.merge(g)
        session.commit()
    else:
        logger.error(thing)


def main(arguments):
    queue = Queue()
    if arguments.max_game_id is None:
        if isinstance(arguments.game_id, int):
            queue.put({'game': arguments.game_id})
        else:
            [queue.put({'game': game_id}) for game_id in arguments.game_id]
    else:
        queue.put({'games': [i + 1 for i in range(arguments.max_game_id)]})
    while not queue.empty():
        process_fetch(queue)


if __name__ == "__main__":
    http = urllib3.PoolManager()
    retries = Retry(connect=5, read=2, redirect=5)
    # execute only if run as a script
    parser = argparse.ArgumentParser(prog='bgg_scrap')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-m", "--max-game-id", type=int, nargs='?', const=42,
                       help="Parse all the games up to MAX_GAME_ID (~300000)")
    group.add_argument("-i", "--game-id", type=int, nargs='+', default=42,
                       help="Parse only GAME_ID")
    parser.add_argument('-fr', action="store_true",
                        help="Use French DB names")
    parser.add_argument('-d', action="store_true",
                        help="Debug")
    parser.add_argument('-dsql', action="store_true",
                        help="Debug SQL")
    parser.add_argument('-v', action="store_true",
                        help="Verbose")
    # Actual max right now : 300000
    args = parser.parse_args()
    from bgg_scrap.models.meta import Base

    if args.fr:
        from bgg_scrap.models.db_fr import *

        engine = create_engine('sqlite:///bgg_fr.sqlite', echo=args.dsql)
    else:
        from bgg_scrap.models.db_en import *

        engine = create_engine('sqlite:///bgg_en.sqlite', echo=args.dsql)
    if args.d:
        engine = create_engine('sqlite:///:memory:', echo=args.dsql)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    verbose = args.v

    logger = logging.getLogger(__name__)
    if args.d:
        logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)

    main(args)

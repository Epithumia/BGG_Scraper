from sqlalchemy import Column, Integer, String, Float, Table
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

from meta import Base

# Base = declarative_base()

artist_table = Table('GameArtist', Base.metadata,
                     Column('game_id', Integer, ForeignKey('Game.id'), nullable=False, primary_key=True),
                     Column('artist_id', Integer, ForeignKey('Person.id'), nullable=False, primary_key=True))

designer_table = Table('GameDesigner', Base.metadata,
                       Column('game_id', Integer, ForeignKey('Game.id'), nullable=False, primary_key=True),
                       Column('designer_id', Integer, ForeignKey('Person.id'), nullable=False, primary_key=True))

producer_table = Table('GameProducer', Base.metadata,
                       Column('game_id', Integer, ForeignKey('Game.id'), nullable=False, primary_key=True),
                       Column('designer_id', Integer, ForeignKey('Person.id'), nullable=False, primary_key=True))

publisher_table = Table('GamePublisher', Base.metadata,
                        Column('game_id', Integer, ForeignKey('Game.id'), nullable=False, primary_key=True),
                        Column('publisher_id', Integer, ForeignKey('Company.id'), nullable=False, primary_key=True))

developer_table = Table('GameDeveloper', Base.metadata,
                        Column('game_id', Integer, ForeignKey('Game.id'), nullable=False, primary_key=True),
                        Column('developer_id', Integer, ForeignKey('Company.id'), nullable=False, primary_key=True))

mechanics_table = Table('GameMechanics', Base.metadata,
                        Column('game_id', Integer, ForeignKey('Game.id'), nullable=False, primary_key=True),
                        Column('property_id', Integer, ForeignKey('Property.id'), nullable=False, primary_key=True))

category_table = Table('GameCategory', Base.metadata,
                       Column('game_id', Integer, ForeignKey('Game.id'), nullable=False, primary_key=True),
                       Column('property_id', Integer, ForeignKey('Property.id'), nullable=False, primary_key=True))

family_table = Table('GameFamily', Base.metadata,
                     Column('game_id', Integer, ForeignKey('Game.id'), nullable=False,
                            primary_key=True),
                     Column('family_id', Integer, ForeignKey('Family.id'), nullable=False,
                            primary_key=True))

subdomain_table = Table('GameSubDomain', Base.metadata,
                        Column('game_id', Integer, ForeignKey('Game.id'), nullable=False,
                               primary_key=True),
                        Column('subdomain_id', Integer, ForeignKey('Family.id'), nullable=False,
                               primary_key=True))

contains_table = Table('Contains', Base.metadata,
                       Column('contains_id', Integer, ForeignKey('Game.id'), nullable=False,
                              primary_key=True),
                       Column('contained_id', Integer, ForeignKey('Game.id'), nullable=False,
                              primary_key=True))

reimplements_table = Table('Reimplements', Base.metadata,
                           Column('reimplements_id', Integer, ForeignKey('Game.id'), nullable=False,
                                  primary_key=True),
                           Column('reimplemented_id', Integer, ForeignKey('Game.id'), nullable=False,
                                  primary_key=True))

expands_table = Table('Expands', Base.metadata,
                      Column('expands_id', Integer, ForeignKey('Game.id'), nullable=False,
                             primary_key=True),
                      Column('expanded_id', Integer, ForeignKey('Game.id'), nullable=False,
                             primary_key=True))

bg_vg_table = Table('VGAdaptation', Base.metadata,
                    Column('adapts_id', Integer, ForeignKey('Game.id'), nullable=False,
                           primary_key=True),
                    Column('adapted_id', Integer, ForeignKey('Game.id'), nullable=False,
                           primary_key=True))


# TODO: genre_table
# TODO: series_table
# TODO: settings_table


class Verbosity(Base):
    __tablename__ = 'LanguageDependency'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)


class Company(Base):
    __tablename__ = 'Company'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    website = Column(String, name='SiteWebCompagnie')

    boardgames = relationship('BoardGame',
                              secondary=publisher_table,
                              backref="publishers")

    boardgameaccessories = relationship('BoardGameAccessory',
                                        secondary=publisher_table,
                                        backref="publishers")

    videogames_developed = relationship('VideoGame',
                                        secondary=developer_table,
                                        backref="developers")

    videogames_published = relationship('VideoGame',
                                        secondary=publisher_table,
                                        backref="publishers")

    rpgs = relationship('RolePlayingGame',
                        secondary=publisher_table,
                        backref="publishers")


class Person(Base):
    __tablename__ = 'Person'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Specific to BoardGames
    boardgames_artist = relationship('BoardGame',
                                     secondary=artist_table,
                                     backref='artists')
    boardgames_designer = relationship('BoardGame',
                                       secondary=designer_table,
                                       backref='designers')

    # Specific to BG accesories
    accessory_artist = relationship('BoardGameAccessory',
                                    secondary=artist_table,
                                    backref='artists')
    accessory_designer = relationship('BoardGameAccessory',
                                      secondary=designer_table,
                                      backref='designers')

    # Specific to rpgitems
    rpg_artist = relationship('RolePlayingGame',
                              secondary=artist_table,
                              backref='artists')
    rpg_designer = relationship('RolePlayingGame',
                                secondary=designer_table,
                                backref='designers')
    rpg_producer = relationship('RolePlayingGame',
                                secondary=producer_table,
                                backref='producers')


class Property(Base):
    __tablename__ = 'Property'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column('type', String(50))
    __mapper_args__ = {'polymorphic_on': type}


class Mechanic(Property):
    boardgames = relationship('BoardGame',
                              secondary=mechanics_table,
                              backref='mechanics')

    roleplayinggames = relationship('RolePlayingGame',
                                    secondary=mechanics_table,
                                    backref='mechanics')

    __mapper_args__ = {'polymorphic_identity': 'gamemechanic'}


class Category(Property):
    boardgames = relationship('BoardGame',
                              secondary=category_table,
                              backref='categories')

    roleplayinggame = relationship('RolePlayingGame',
                                   secondary=category_table,
                                   backref='categories')

    __mapper_args__ = {'polymorphic_identity': 'gamecategory'}


class NbPlayers(Base):
    __tablename__ = 'NbPlayers'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('Game.id'), primary_key=True)
    type = Column('type', String(20))
    min = Column(Integer)
    max = Column(Integer)
    __mapper_args__ = {'polymorphic_on': type}


class Best(NbPlayers):
    games = relationship('BoardGame', backref="best")
    __mapper_args__ = {'polymorphic_identity': 'best'}


class Recommended(NbPlayers):
    games = relationship('BoardGame', backref="recommended")
    __mapper_args__ = {'polymorphic_identity': 'recommended'}


class Family(Base):
    __tablename__ = 'Family'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subtype = Column(String, nullable=False)
    description = Column(String, name='Description')

    __mapper_args__ = {'polymorphic_on': subtype,
                       'polymorphic_identity': 'family'}


class BoardGameSubdomain(Family):
    boardgames = relationship('BoardGame',
                              secondary=subdomain_table,
                              backref="boardgamesubdomains")

    __mapper_args__ = {'polymorphic_identity': 'boardgamesubdomain'}


class BoardGameFamily(Family):
    boardgames = relationship('BoardGame',
                              secondary=family_table,
                              backref="boardgamefamilies")

    __mapper_args__ = {'polymorphic_identity': 'boardgamefamily'}


class Game(Base):
    __tablename__ = 'Game'

    # Generic data
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    # Common stats
    rank = Column(Integer)
    usersrated = Column(Integer)
    average_rating = Column(Float)
    bayes_average_rating = Column(Float)

    __mapper_args__ = {'polymorphic_on': type}


class BoardGame(Game):

    @declared_attr
    def yearpublished(selfself):
        return Game.__table__.c.get('yearpublished', Column(Integer))

    # Specific to BoardGames
    @declared_attr
    def minplayers(self):
        return Game.__table__.c.get('minplayers', Column(Integer))

    @declared_attr
    def maxplayers(self):
        return Game.__table__.c.get('maxplayers', Column(Integer))

    minplaytime = Column(Integer)
    maxplaytime = Column(Integer)
    minage = Column(Integer)
    recommended_age = Column(String)
    id_languagedependency = Column(Integer, ForeignKey(Verbosity.id))
    languagedependency = relationship(Verbosity, backref='boardgames')

    contains = relationship('BoardGame',
                            secondary=contains_table,
                            primaryjoin='BoardGame.id == Contains.c.contains_id',
                            secondaryjoin='BoardGame.id == Contains.c.contained_id',
                            backref="contained")

    reimplements = relationship('Game',
                                secondary=reimplements_table,
                                primaryjoin='BoardGame.id == Reimplements.c.reimplements_id',
                                secondaryjoin='BoardGame.id == Reimplements.c.reimplemented_id',
                                backref="reimplemented")

    expands = relationship('Game',
                           secondary=expands_table,
                           primaryjoin='BoardGame.id == Expands.c.expands_id',
                           secondaryjoin='BoardGame.id == Expands.c.expanded_id',
                           backref="expanded")

    # TODO: boardgameversion -> version
    # TODO: boardgameintegration -> boardgame
    # TODO: boardgamesubdomain -> family
    # TODO: boardgameaccessory -> bgaccessory

    __mapper_args__ = {'polymorphic_identity': 'boardgame'}


class BoardGameAccessory(Game):

    @declared_attr
    def yearpublished(self):
        return Game.__table__.c.get('yearpublished', Column(Integer))

    # TODO: bgaccessoryversion -> version

    __mapper_args__ = {'polymorphic_identity': 'boardgameaccessory'}


class VideoGame(Game):
    @declared_attr
    def minplayers(self):
        return Game.__table__.c.get('minplayers', Column(Integer))

    @declared_attr
    def maxplayers(self):
        return Game.__table__.c.get('maxplayers', Column(Integer))

    @declared_attr
    def yearpublished(self):
        """
        Actually a date (YYYY-MM-DD) that needs to be parsed
        """
        return Game.__table__.c.get('yearpublished', Column(Integer))

    # TODO: videogameplatform -> family
    # TODO: videogamegenre -> property
    # TODO: videogametheme -> property
    # TODO: videogamefranchise -> family
    # TODO: videogameseries -> family
    # TODO: videogamemode -> property

    # TODO: expandsvideogame -> videogame
    # TODO: contains -> videogame

    adapts = relationship('Game',
                          secondary=bg_vg_table,
                          primaryjoin='VideoGame.id == VGAdaptation.c.adapts_id',
                          secondaryjoin='BoardGame.id == VGAdaptation.c.adapted_id',
                          backref="vgadaptation")

    __mapper_args__ = {'polymorphic_identity': 'videogame'}


class RolePlayingGame(Game):

    @declared_attr
    def yearpublished(selfself):
        return Game.__table__.c.get('yearpublished', Column(Integer))

    # TODO: rpg -> family
    # TODO: rpggenre -> family
    # TODO: rpgsetting -> family
    # TODO: rpgseries -> family

    __mapper_args__ = {'polymorphic_identity': 'rpgitem'}


class RPGIssue(Game):
    __mapper_args__ = {'polymorphic_identity': 'rpgissue'}

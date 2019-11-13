from sqlalchemy import Column, Integer, String, Float, Table
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

from bgg_scrap.models.meta import Base

# TODO: translate

artist_table = Table('GameArtist', Base.metadata,
                     Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                     Column('artist_id', Integer, ForeignKey('Personne.IdPersonne'), nullable=False, primary_key=True))

designer_table = Table('GameDesigner', Base.metadata,
                       Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                       Column('designer_id', Integer, ForeignKey('Personne.IdPersonne'), nullable=False, primary_key=True))

producer_table = Table('GameProducer', Base.metadata,
                       Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                       Column('designer_id', Integer, ForeignKey('Personne.IdPersonne'), nullable=False, primary_key=True))

publisher_table = Table('GamePublisher', Base.metadata,
                        Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                        Column('publisher_id', Integer, ForeignKey('Compagnie.IdCompagnie'), nullable=False, primary_key=True))

developer_table = Table('GameDeveloper', Base.metadata,
                        Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                        Column('developer_id', Integer, ForeignKey('Compagnie.IdCompagnie'), nullable=False, primary_key=True))

mechanics_table = Table('GameMechanics', Base.metadata,
                        Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                        Column('property_id', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False, primary_key=True))

category_table = Table('GameCategory', Base.metadata,
                       Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                       Column('property_id', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False, primary_key=True))

family_table = Table('GameFamily', Base.metadata,
                     Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                            primary_key=True),
                     Column('family_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                            primary_key=True))

subdomain_table = Table('GameSubDomain', Base.metadata,
                        Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                               primary_key=True),
                        Column('subdomain_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                               primary_key=True))

contains_table = Table('Contenu', Base.metadata,
                       Column('contains_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                              primary_key=True),
                       Column('contained_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                              primary_key=True))

reimplements_table = Table('Reimplementation', Base.metadata,
                           Column('reimplements_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                  primary_key=True),
                           Column('reimplemented_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                  primary_key=True))

expands_table = Table('Expands', Base.metadata,
                      Column('expands_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                             primary_key=True),
                      Column('expanded_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                             primary_key=True))

integration_table = Table('Integration', Base.metadata,
                          Column('integrates_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                 primary_key=True),
                          Column('integrated_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                 primary_key=True))

bg_vg_table = Table('VGAdaptation', Base.metadata,
                    Column('adapts_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                           primary_key=True),
                    Column('adapted_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                           primary_key=True))

bg_accessory_table = Table('EstAccessoire', Base.metadata,
                           Column('accessory_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                  primary_key=True),
                           Column('boardgame_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                  primary_key=True))

theme_table = Table('Theme', Base.metadata,
                    Column('theme_id', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False,
                           primary_key=True),
                    Column('videogame_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                           primary_key=True))

mode_table = Table('Mode', Base.metadata,
                   Column('mode_id', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False,
                          primary_key=True),
                   Column('videogame_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                          primary_key=True))

vggenre_table = Table('VGGenre', Base.metadata,
                      Column('genre_id', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False,
                             primary_key=True),
                      Column('videogame_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                             primary_key=True))

language_table = Table('BoardGameLanguage', Base.metadata,
                       Column('language_id', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False,
                              primary_key=True),
                       Column('boardgame_id', Integer, ForeignKey('Version.id'), nullable=False,
                              primary_key=True))

rpggenre_table = Table('RPGGenre', Base.metadata,
                       Column('genre_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                              primary_key=True),
                       Column('roleplayinggame_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                              primary_key=True))

series_table = Table('GameSeries', Base.metadata,
                     Column('series_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                            primary_key=True),
                     Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                            primary_key=True))

franchise_table = Table('Franchise', Base.metadata,
                        Column('franchise_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                               primary_key=True),
                        Column('videogame_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                               primary_key=True))

platform_table = Table('Platform', Base.metadata,
                       Column('platform_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                              primary_key=True),
                       Column('videogame_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                              primary_key=True))

rpgsetting_table = Table('Setting', Base.metadata,
                         Column('setting_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                                primary_key=True),
                         Column('roleplayinggame_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                primary_key=True))

rpg_table = Table('RPGr', Base.metadata,
                  Column('rpg_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                         primary_key=True),
                  Column('roleplayinggame_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                         primary_key=True))

version_table = Table('GameVersion', Base.metadata,
                      Column('version_id', Integer, ForeignKey('Version.id'), nullable=False,
                             primary_key=True),
                      Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                             primary_key=True))

publisher_version_table = Table('PublisherVersion', Base.metadata,
                                Column('version_id', Integer, ForeignKey('Version.id'), nullable=False,
                                       primary_key=True),
                                Column('publisher_id', Integer, ForeignKey('Compagnie.IdCompagnie'), nullable=False,
                                       primary_key=True))

artist_version_table = Table('ArtistVersion', Base.metadata,
                             Column('version_id', Integer, ForeignKey('Version.id'), nullable=False,
                                    primary_key=True),
                             Column('artist_id', Integer, ForeignKey('Personne.IdPersonne'), nullable=False,
                                    primary_key=True))


class Verbosity(Base):
    __tablename__ = 'DependanceLangage'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)


class Company(Base):
    __tablename__ = 'Compagnie'

    id = Column(Integer, primary_key=True, name='IdCompagnie')
    name = Column(String, nullable=False, name='NomCompagnie')
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
    __tablename__ = 'Personne'

    id = Column(Integer, primary_key=True, name='IdPersonne')
    name = Column(String, nullable=False, name='NomPersonne')

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
    __tablename__ = 'Propriete'

    id = Column(Integer, primary_key=True, name='IdPropriete')
    name = Column(String, nullable=False, name='NomPropriete')
    type = Column(String(50), name='TypePropriete')
    __mapper_args__ = {'polymorphic_on': type}


class Mechanic(Property):
    boardgames = relationship('BoardGame',
                              secondary=mechanics_table,
                              backref='mechanics')

    roleplayinggames = relationship('RolePlayingGame',
                                    secondary=mechanics_table,
                                    backref='mechanics')

    __mapper_args__ = {'polymorphic_identity': 'mecaniquejeu'}


class Category(Property):
    boardgames = relationship('BoardGame',
                              secondary=category_table,
                              backref='categories')

    roleplayinggame = relationship('RolePlayingGame',
                                   secondary=category_table,
                                   backref='categories')

    __mapper_args__ = {'polymorphic_identity': 'categoriejeu'}


class VideoGameGenre(Property):
    videogames = relationship('VideoGame',
                              secondary=vggenre_table,
                              backref='genres')

    __mapper_args__ = {'polymorphic_identity': 'genrejeuvideo'}


class VideoGameTheme(Property):
    videogames = relationship('VideoGame',
                              secondary=theme_table,
                              backref='themes')

    __mapper_args__ = {'polymorphic_identity': 'themejeuvideo'}


class VideoGameMode(Property):
    videogames = relationship('VideoGame',
                              secondary=mode_table,
                              backref='modes')

    __mapper_args__ = {'polymorphic_identity': 'modejeuvideo'}


class Language(Property):
    versions = relationship('Version',
                            secondary=language_table,
                            backref='languages')

    __mapper_args__ = {'polymorphic_identity': 'langage'}


class NbPlayers(Base):
    __tablename__ = 'NbJoueurs'

    id = Column(Integer, primary_key=True, name='IdNbJoueurs')
    game_id = Column(Integer, ForeignKey('Jeu.IdJeu'), primary_key=True, name='IdJeu')
    type = Column('type', String(20))
    min = Column(Integer)
    max = Column(Integer)
    __mapper_args__ = {'polymorphic_on': type}


class Best(NbPlayers):
    games = relationship('BoardGame', backref="best")
    __mapper_args__ = {'polymorphic_identity': 'meilleur'}


class Recommended(NbPlayers):
    games = relationship('BoardGame', backref="recommended")
    __mapper_args__ = {'polymorphic_identity': 'recommande'}


class Family(Base):
    __tablename__ = 'Famille'

    id = Column(Integer, primary_key=True, name='IdFamille')
    name = Column(String, nullable=False, name='NomFamille')
    subtype = Column(String, nullable=False, name='TypeFamille')
    description = Column(String, name='Description')

    __mapper_args__ = {'polymorphic_on': subtype,
                       'polymorphic_identity': 'famille'}


class BoardGameSubdomain(Family):
    boardgames = relationship('BoardGame',
                              secondary=subdomain_table,
                              backref="boardgamesubdomains")

    __mapper_args__ = {'polymorphic_identity': 'sous-domaine jeu de société'}


class BoardGameFamily(Family):
    boardgames = relationship('BoardGame',
                              secondary=family_table,
                              backref="boardgamefamilies")

    __mapper_args__ = {'polymorphic_identity': 'famille jeu de société'}


class VGFranchise(Family):
    videogames = relationship('VideoGame',
                              secondary=franchise_table,
                              backref="franchises")

    __mapper_args__ = {'polymorphic_identity': 'franchise de jeu vidéo'}


class VGPlatforms(Family):
    videogames = relationship('VideoGame',
                              secondary=platform_table,
                              backref="platforms")

    __mapper_args__ = {'polymorphic_identity': 'plateforme de jeu vidéo'}


class VGSeries(Family):
    videogames = relationship('VideoGame',
                              secondary=series_table,
                              backref="series")

    __mapper_args__ = {'polymorphic_identity': 'série de jeu vidéo'}


class RPG(Family):
    rpgs = relationship('RolePlayingGame',
                        secondary=rpg_table,
                        backref="rpgs")

    __mapper_args__ = {'polymorphic_identity': 'rpg'}


class RPGGenre(Family):
    rpgs = relationship('RolePlayingGame',
                        secondary=rpggenre_table,
                        backref="genres")

    __mapper_args__ = {'polymorphic_identity': 'Genre RPG'}


class RPGSetting(Family):
    rpgs = relationship('RolePlayingGame',
                        secondary=rpgsetting_table,
                        backref="settings")

    __mapper_args__ = {'polymorphic_identity': 'rpgsetting'}


class RPGSeries(Family):
    rpgs = relationship('RolePlayingGame',
                        secondary=series_table,
                        backref="series")

    __mapper_args__ = {'polymorphic_identity': 'Série RPG'}


class Game(Base):
    __tablename__ = 'Jeu'

    # Generic data
    id = Column(Integer, primary_key=True, name='IdJeu')
    name = Column(String, nullable=False, name='NomJeu')
    type = Column(String, nullable=False, name='TypeJeu')

    # Common stats
    rank = Column(Integer, name='Rang')
    usersrated = Column(Integer, name='NoteUtilisateurs')
    average_rating = Column(Float, name='NoteMoyenne')
    bayes_average_rating = Column(Float, name='NotePondérée')

    __mapper_args__ = {'polymorphic_on': type}


class BoardGame(Game):

    @declared_attr
    def yearpublished(self):
        return Game.__table__.c.get('yearpublished', Column(Integer))

    # Specific to BoardGames
    @declared_attr
    def minplayers(self):
        return Game.__table__.c.get('minplayers', Column(Integer))

    @declared_attr
    def maxplayers(self):
        return Game.__table__.c.get('maxplayers', Column(Integer))

    minplaytime = Column(Integer, name='DuréeMini')
    maxplaytime = Column(Integer, name='DuréeMaxi')
    minage = Column(Integer, name='AgeMini')
    recommended_age = Column(String, name='AgeRecommandé')
    id_languagedependency = Column(Integer, ForeignKey(Verbosity.id), name='IdDepLang')
    languagedependency = relationship(Verbosity, backref='boardgames')

    contains = relationship('BoardGame',
                            secondary=contains_table,
                            primaryjoin='BoardGame.id == Contenu.c.contains_id',
                            secondaryjoin='BoardGame.id == Contenu.c.contained_id',
                            backref="contained")

    reimplements = relationship('BoardGame',
                                secondary=reimplements_table,
                                primaryjoin='BoardGame.id == Reimplementation.c.reimplements_id',
                                secondaryjoin='BoardGame.id == Reimplementation.c.reimplemented_id',
                                backref="reimplemented")

    expands = relationship('BoardGame',
                           secondary=expands_table,
                           primaryjoin='BoardGame.id == Expands.c.expands_id',
                           secondaryjoin='BoardGame.id == Expands.c.expanded_id',
                           backref="expanded")

    integrates = relationship('BoardGame',
                              secondary=integration_table,
                              primaryjoin='BoardGame.id == Integration.c.integrates_id',
                              secondaryjoin='BoardGame.id == Integration.c.integrated_id',
                              backref="integrated")

    boardgameaccessories = relationship('Game',
                                        secondary=bg_accessory_table,
                                        primaryjoin='BoardGameAccessory.id == EstAccessoire.c.accessory_id',
                                        secondaryjoin='BoardGame.id == EstAccessoire.c.boardgame_id',
                                        backref="boardgames")

    __mapper_args__ = {'polymorphic_identity': 'Jeu de Société'}


class BoardGameAccessory(Game):

    @declared_attr
    def yearpublished(self):
        return Game.__table__.c.get('yearpublished', Column(Integer))

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

    contains = relationship('VideoGame',
                            secondary=contains_table,
                            primaryjoin='VideoGame.id == Contenu.c.contains_id',
                            secondaryjoin='VideoGame.id == Contenu.c.contained_id',
                            backref="contained")

    adapts = relationship('BoardGame',
                          secondary=bg_vg_table,
                          primaryjoin='VideoGame.id == VGAdaptation.c.adapts_id',
                          secondaryjoin='BoardGame.id == VGAdaptation.c.adapted_id',
                          backref="vgadaptation")

    expands = relationship('VideoGame',
                           secondary=expands_table,
                           primaryjoin='VideoGame.id == Expands.c.expands_id',
                           secondaryjoin='VideoGame.id == Expands.c.expanded_id',
                           backref="expanded")

    __mapper_args__ = {'polymorphic_identity': 'videogame'}


class RolePlayingGame(Game):

    @declared_attr
    def yearpublished(self):
        return Game.__table__.c.get('yearpublished', Column(Integer))

    __mapper_args__ = {'polymorphic_identity': 'rpgitem'}


class RPGIssue(Game):
    __mapper_args__ = {'polymorphic_identity': 'rpgissue'}


class Version(Base):
    __tablename__ = 'Version'

    id = Column(Integer, primary_key=True)
    linkedname = Column(String)
    versionname = Column(String)
    yearpublished = Column(Integer)
    subtype = Column(String)

    __mapper_args__ = {'polymorphic_on': subtype,
                       'polymorphic_identity': 'version'}


class BoardGameVersion(Version):
    boardgames = relationship('BoardGame',
                              secondary=version_table,
                              backref="versions")

    publishers = relationship('Company',
                              secondary=publisher_version_table,
                              backref="versions")

    artists = relationship('Person',
                           secondary=artist_version_table,
                           backref="versions")

    __mapper_args__ = {'polymorphic_identity': 'boardgameversion'}


class BoardGameAccessoryVersion(Version):
    boardgameaccessories = relationship('BoardGameAccessory',
                                        secondary=version_table,
                                        backref="versions")

    __mapper_args__ = {'polymorphic_identity': 'boardgameaccessoryversion'}

from sqlalchemy import Column, Integer, String, Float, Table
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

from bgg_scrap.models.meta import Base

artist_table = Table('ArtisteJeu', Base.metadata,
                     Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                     Column('IdArtiste', Integer, ForeignKey('Personne.IdPersonne'), nullable=False, primary_key=True))

# TODO: translate table, column1, column2
designer_table = Table('GameDesigner', Base.metadata,
                       Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                       Column('designer_id', Integer, ForeignKey('Personne.IdPersonne'), nullable=False,
                              primary_key=True))

# TODO: translate table
producer_table = Table('GameProducer', Base.metadata,
                       Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                       Column('IdProducteur', Integer, ForeignKey('Personne.IdPersonne'), nullable=False,
                              primary_key=True))

publisher_table = Table('EditeurJeu', Base.metadata,
                        Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                        Column('IdEditeur', Integer, ForeignKey('Compagnie.IdCompagnie'), nullable=False,
                               primary_key=True))

# TODO: translate table, column1, column2
developer_table = Table('GameDeveloper', Base.metadata,
                        Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                        Column('developer_id', Integer, ForeignKey('Compagnie.IdCompagnie'), nullable=False,
                               primary_key=True))

mechanics_table = Table('MecaniqueJeu', Base.metadata,
                        Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                        Column('IdMecanique', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False,
                               primary_key=True))

category_table = Table('CategorieJeu', Base.metadata,
                       Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                       Column('IdCategorie', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False,
                              primary_key=True))

# TODO: translate table, column1, column2
family_table = Table('GameFamily', Base.metadata,
                     Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                            primary_key=True),
                     Column('family_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                            primary_key=True))

subdomain_table = Table('SousDomaineJeu', Base.metadata,
                        Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                               primary_key=True),
                        Column('IdSousDomaine', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                               primary_key=True))

# TODO: translate column1, column2
contains_table = Table('Contenu', Base.metadata,
                       Column('contains_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                              primary_key=True),
                       Column('contained_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                              primary_key=True))

# TODO: translate column1, column2
reimplements_table = Table('Reimplementation', Base.metadata,
                           Column('reimplements_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                  primary_key=True),
                           Column('reimplemented_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                  primary_key=True))

# TODO: translate column1, column2
expands_table = Table('Expansion', Base.metadata,
                      Column('expands_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                             primary_key=True),
                      Column('expanded_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                             primary_key=True))

# TODO: translate column1, column2
integration_table = Table('Integration', Base.metadata,
                          Column('integrates_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                 primary_key=True),
                          Column('integrated_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                 primary_key=True))

# TODO: translate table, column1, column2
bg_vg_table = Table('VGAdaptation', Base.metadata,
                    Column('adapts_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                           primary_key=True),
                    Column('adapted_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                           primary_key=True))

bg_accessory_table = Table('EstAccessoire', Base.metadata,
                           Column('IdAccessoire', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                  primary_key=True),
                           Column('IdJeuSociete', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                  primary_key=True))

theme_table = Table('Theme', Base.metadata,
                    Column('IdTheme', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False,
                           primary_key=True),
                    Column('IdJeuVideo', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                           primary_key=True))

mode_table = Table('Mode', Base.metadata,
                   Column('IdMode', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False,
                          primary_key=True),
                   Column('IdJeuVideo', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                          primary_key=True))

vggenre_table = Table('GenreJeuVideo', Base.metadata,
                      Column('IdGenre', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False,
                             primary_key=True),
                      Column('IdJeuVideo', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                             primary_key=True))

language_table = Table('Traduction', Base.metadata,
                       Column('IdLangage', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False,
                              primary_key=True),
                       Column('IdVersion', Integer, ForeignKey('Version.IdVersion'), nullable=False,
                              primary_key=True))

# TODO: translate table, column1, column2
rpggenre_table = Table('RPGGenre', Base.metadata,
                       Column('genre_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                              primary_key=True),
                       Column('roleplayinggame_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                              primary_key=True))

# TODO: translate table, column1, column2
series_table = Table('GameSeries', Base.metadata,
                     Column('series_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                            primary_key=True),
                     Column('game_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                            primary_key=True))

franchise_table = Table('Franchise', Base.metadata,
                        Column('IdFranchise', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                               primary_key=True),
                        Column('IdJeuvideo', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                               primary_key=True))

platform_table = Table('Plateforme', Base.metadata,
                       Column('IdPlateforme', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                              primary_key=True),
                       Column('IdJeuVideo', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                              primary_key=True))

# TODO: translate table, column1, column2
rpgsetting_table = Table('Setting', Base.metadata,
                         Column('setting_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                                primary_key=True),
                         Column('roleplayinggame_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                primary_key=True))

# TODO: translate table, column1, column2
rpg_table = Table('RPGr', Base.metadata,
                  Column('rpg_id', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                         primary_key=True),
                  Column('roleplayinggame_id', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                         primary_key=True))

version_table = Table('VersionJeu', Base.metadata,
                      Column('IdVersion', Integer, ForeignKey('Version.IdVersion'), nullable=False,
                             primary_key=True),
                      Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                             primary_key=True))

publisher_version_table = Table('EditionVersion', Base.metadata,
                                Column('IdVersion', Integer, ForeignKey('Version.IdVersion'), nullable=False,
                                       primary_key=True),
                                Column('IdEditeur', Integer, ForeignKey('Compagnie.IdCompagnie'), nullable=False,
                                       primary_key=True))

artist_version_table = Table('ArtisteVersion', Base.metadata,
                             Column('IdVersion', Integer, ForeignKey('Version.IdVersion'), nullable=False,
                                    primary_key=True),
                             Column('IdArtiste', Integer, ForeignKey('Personne.IdPersonne'), nullable=False,
                                    primary_key=True))


class Verbosity(Base):
    __tablename__ = 'DependanceLangage'

    id = Column(Integer, primary_key=True, autoincrement=True, name='IdDependance')
    text = Column(String, nullable=False, name='LibelleDependance')


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

    __mapper_args__ = {'polymorphic_identity': 'Mécanique de Jeu'}


class Category(Property):
    boardgames = relationship('BoardGame',
                              secondary=category_table,
                              backref='categories')

    roleplayinggame = relationship('RolePlayingGame',
                                   secondary=category_table,
                                   backref='categories')

    __mapper_args__ = {'polymorphic_identity': 'Catégorie de Jeu'}


class VideoGameGenre(Property):
    videogames = relationship('VideoGame',
                              secondary=vggenre_table,
                              backref='genres')

    __mapper_args__ = {'polymorphic_identity': 'Genre de Jeu Vidéo'}


class VideoGameTheme(Property):
    videogames = relationship('VideoGame',
                              secondary=theme_table,
                              backref='themes')

    __mapper_args__ = {'polymorphic_identity': 'Thème de Jeu Vidéo'}


class VideoGameMode(Property):
    videogames = relationship('VideoGame',
                              secondary=mode_table,
                              backref='modes')

    __mapper_args__ = {'polymorphic_identity': 'Mode de Jeu Vidéo'}


class Language(Property):
    versions = relationship('Version',
                            secondary=language_table,
                            backref='languages')

    __mapper_args__ = {'polymorphic_identity': 'Langage'}


class NbPlayers(Base):
    __tablename__ = 'NbJoueurs'

    id = Column(Integer, primary_key=True, name='IdNbJoueurs')
    game_id = Column(Integer, ForeignKey('Jeu.IdJeu'), primary_key=True, name='IdJeu')
    type = Column('Type', String(20))
    min = Column(Integer)
    max = Column(Integer)
    __mapper_args__ = {'polymorphic_on': type}


class Best(NbPlayers):
    games = relationship('BoardGame', backref="best")
    __mapper_args__ = {'polymorphic_identity': 'Meilleur'}


class Recommended(NbPlayers):
    games = relationship('BoardGame', backref="recommended")
    __mapper_args__ = {'polymorphic_identity': 'Recommandé'}


class Family(Base):
    __tablename__ = 'Famille'

    id = Column(Integer, primary_key=True, name='IdFamille')
    name = Column(String, nullable=False, name='NomFamille')
    subtype = Column(String, nullable=False, name='TypeFamille')
    description = Column(String, name='Description')

    __mapper_args__ = {'polymorphic_on': subtype,
                       'polymorphic_identity': 'Famille'}


class BoardGameSubdomain(Family):
    boardgames = relationship('BoardGame',
                              secondary=subdomain_table,
                              backref="boardgamesubdomains")

    __mapper_args__ = {'polymorphic_identity': 'Sous-domaine jeu de société'}


class BoardGameFamily(Family):
    boardgames = relationship('BoardGame',
                              secondary=family_table,
                              backref="boardgamefamilies")

    __mapper_args__ = {'polymorphic_identity': 'Famille jeu de société'}


class VGFranchise(Family):
    videogames = relationship('VideoGame',
                              secondary=franchise_table,
                              backref="franchises")

    __mapper_args__ = {'polymorphic_identity': 'Franchise de jeu vidéo'}


class VGPlatforms(Family):
    videogames = relationship('VideoGame',
                              secondary=platform_table,
                              backref="platforms")

    __mapper_args__ = {'polymorphic_identity': 'Plateforme de jeu vidéo'}


class VGSeries(Family):
    videogames = relationship('VideoGame',
                              secondary=series_table,
                              backref="series")

    __mapper_args__ = {'polymorphic_identity': 'Série de jeu vidéo'}


class RPG(Family):
    rpgs = relationship('RolePlayingGame',
                        secondary=rpg_table,
                        backref="rpgs")

    __mapper_args__ = {'polymorphic_identity': 'Famille RPG'}


class RPGGenre(Family):
    rpgs = relationship('RolePlayingGame',
                        secondary=rpggenre_table,
                        backref="genres")

    __mapper_args__ = {'polymorphic_identity': 'Genre RPG'}


class RPGSetting(Family):
    rpgs = relationship('RolePlayingGame',
                        secondary=rpgsetting_table,
                        backref="settings")

    __mapper_args__ = {'polymorphic_identity': 'Cadre RPG'}


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
    bayes_average_rating = Column(Float, name='NotePonderee')

    __mapper_args__ = {'polymorphic_on': type}


class BoardGame(Game):

    @declared_attr
    def yearpublished(self):
        return Game.__table__.c.get('AnneePublicationJeu', Column(Integer, name='AnneePublicationJeu'))

    # Specific to BoardGames
    @declared_attr
    def minplayers(self):
        return Game.__table__.c.get('NbJoueursMin', Column(Integer, name='NbJoueursMin'))

    @declared_attr
    def maxplayers(self):
        return Game.__table__.c.get('NbJoueursMax', Column(Integer, name='NbJoueursMax'))

    minplaytime = Column(Integer, name='DureeMini')
    maxplaytime = Column(Integer, name='DureeMaxi')
    minage = Column(Integer, name='AgeMini')
    recommended_age = Column(String, name='AgeRecommande')
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
                           primaryjoin='BoardGame.id == Expansion.c.expands_id',
                           secondaryjoin='BoardGame.id == Expansion.c.expanded_id',
                           backref="expanded")

    integrates = relationship('BoardGame',
                              secondary=integration_table,
                              primaryjoin='BoardGame.id == Integration.c.integrates_id',
                              secondaryjoin='BoardGame.id == Integration.c.integrated_id',
                              backref="integrated")

    boardgameaccessories = relationship('Game',
                                        secondary=bg_accessory_table,
                                        primaryjoin='BoardGameAccessory.id == EstAccessoire.c.IdAccessoire',
                                        secondaryjoin='BoardGame.id == EstAccessoire.c.IdJeuSociete',
                                        backref="boardgames")

    __mapper_args__ = {'polymorphic_identity': 'Jeu de Société'}


class BoardGameAccessory(Game):

    @declared_attr
    def yearpublished(self):
        return Game.__table__.c.get('AnneePublicationJeu', Column(Integer, name='AnneePublicationJeu'))

    __mapper_args__ = {'polymorphic_identity': 'Accessoire de Jeu de Société'}


class VideoGame(Game):
    @declared_attr
    def minplayers(self):
        return Game.__table__.c.get('NbJoueursMin', Column(Integer, name='NbJoueursMin'))

    @declared_attr
    def maxplayers(self):
        return Game.__table__.c.get('NbJoueursMax', Column(Integer, name='NbJoueursMax'))

    @declared_attr
    def yearpublished(self):
        """
        Actually a date (YYYY-MM-DD) that needs to be parsed
        """
        return Game.__table__.c.get('AnneePublicationJeu', Column(Integer, name='AnneePublicationJeu'))

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
                           primaryjoin='VideoGame.id == Expansion.c.expands_id',
                           secondaryjoin='VideoGame.id == Expansion.c.expanded_id',
                           backref="expanded")

    __mapper_args__ = {'polymorphic_identity': 'videogame'}


class RolePlayingGame(Game):

    @declared_attr
    def yearpublished(self):
        return Game.__table__.c.get('AnneePublicationJeu', Column(Integer, name='AnneePublicationJeu'))

    __mapper_args__ = {'polymorphic_identity': 'JDR'}


class RPGIssue(Game):
    __mapper_args__ = {'polymorphic_identity': 'Revue JDR'}


class Version(Base):
    __tablename__ = 'Version'

    id = Column(Integer, primary_key=True, name='IdVersion')
    linkedname = Column(String, name='NomBaseJeu')
    versionname = Column(String, name='NomVersion')
    yearpublished = Column(Integer, name='AnneePublicationVersion')
    subtype = Column(String, name='TypeVersion')

    __mapper_args__ = {'polymorphic_on': subtype,
                       'polymorphic_identity': 'Version'}


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

    __mapper_args__ = {'polymorphic_identity': 'Version de Jeu de Société'}


class BoardGameAccessoryVersion(Version):
    boardgameaccessories = relationship('BoardGameAccessory',
                                        secondary=version_table,
                                        backref="versions")

    __mapper_args__ = {'polymorphic_identity': 'Version d\'accessoire de Jeu de Société'}

from sqlalchemy import Column, Integer, String, Float, Table
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

from bgg_scraper.models.meta import Base

artist_table = Table('ArtisteJeu', Base.metadata,
                     Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                     Column('IdArtiste', Integer, ForeignKey('Personne.IdPersonne'), nullable=False, primary_key=True))

designer_table = Table('ConcepteurJeu', Base.metadata,
                       Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                       Column('IdConcepteur', Integer, ForeignKey('Personne.IdPersonne'), nullable=False,
                              primary_key=True))

producer_table = Table('ProducteurJeu', Base.metadata,
                       Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                       Column('IdProducteur', Integer, ForeignKey('Personne.IdPersonne'), nullable=False,
                              primary_key=True))

publisher_table = Table('EditeurJeu', Base.metadata,
                        Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                        Column('IdEditeur', Integer, ForeignKey('Compagnie.IdCompagnie'), nullable=False,
                               primary_key=True))

developer_table = Table('DeveloppeurJeu', Base.metadata,
                        Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                        Column('IdDeveloppeur', Integer, ForeignKey('Compagnie.IdCompagnie'), nullable=False,
                               primary_key=True))

mechanics_table = Table('MecaniqueJeu', Base.metadata,
                        Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                        Column('IdMecanique', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False,
                               primary_key=True))

category_table = Table('CategorieJeu', Base.metadata,
                       Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False, primary_key=True),
                       Column('IdCategorie', Integer, ForeignKey('Propriete.IdPropriete'), nullable=False,
                              primary_key=True))

family_table = Table('FamilleJeu', Base.metadata,
                     Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                            primary_key=True),
                     Column('FamilleJeu', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                            primary_key=True))

subdomain_table = Table('SousDomaineJeu', Base.metadata,
                        Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                               primary_key=True),
                        Column('IdSousDomaine', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                               primary_key=True))

contains_table = Table('Contenu', Base.metadata,
                       Column('IdJeuContenant', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                              primary_key=True),
                       Column('IdJeuContenu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                              primary_key=True))

reimplements_table = Table('Reimplementation', Base.metadata,
                           Column('IdReimplementation', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                  primary_key=True),
                           Column('IdJeuBase', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                  primary_key=True))

expands_table = Table('Extension', Base.metadata,
                      Column('IdExtension', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                             primary_key=True),
                      Column('IdJeuBase', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                             primary_key=True))

integration_table = Table('Integration', Base.metadata,
                          Column('IdJeuIntegrateur', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                 primary_key=True),
                          Column('IdJeuIntegre', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                 primary_key=True))

# TODO: check relation sides
bg_vg_table = Table('AdaptationJeuVideo', Base.metadata,
                    Column('IdJeuVideo', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                           primary_key=True),
                    Column('IdJeuPlateauAdapte', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
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

rpggenre_table = Table('GenreJDR', Base.metadata,
                       Column('IgGenre', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                              primary_key=True),
                       Column('IdJDR', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                              primary_key=True))

series_table = Table('SerieJeu', Base.metadata,
                     Column('IdSerie', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                            primary_key=True),
                     Column('IdJeu', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
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

rpgsetting_table = Table('Cadre', Base.metadata,
                         Column('IdCadre', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                                primary_key=True),
                         Column('IdJDR', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
                                primary_key=True))

rpg_table = Table('SystemeJDR', Base.metadata,
                  Column('IdSysteme', Integer, ForeignKey('Famille.IdFamille'), nullable=False,
                         primary_key=True),
                  Column('IdJDR', Integer, ForeignKey('Jeu.IdJeu'), nullable=False,
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
    usersrated = Column(Integer, name='NbNotesUtilisateurs')
    average_rating = Column(Float, name='NoteMoyenne')
    bayes_average_rating = Column(Float, name='NotePonderee')
    complexity = Column(Float, name='Complexite')

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
                            primaryjoin='BoardGame.id == Contenu.c.IdJeuContenant',
                            secondaryjoin='BoardGame.id == Contenu.c.IdJeuContenu',
                            backref="contained")

    reimplements = relationship('BoardGame',
                                secondary=reimplements_table,
                                primaryjoin='BoardGame.id == Reimplementation.c.IdReimplementation',
                                secondaryjoin='BoardGame.id == Reimplementation.c.IdJeuBase',
                                backref="reimplemented")

    expands = relationship('BoardGame',
                           secondary=expands_table,
                           primaryjoin='BoardGame.id == Extension.c.IdExtension',
                           secondaryjoin='BoardGame.id == Extension.c.IdJeuBase',
                           backref="expanded")

    integrates = relationship('BoardGame',
                              secondary=integration_table,
                              primaryjoin='BoardGame.id == Integration.c.IdJeuIntegrateur',
                              secondaryjoin='BoardGame.id == Integration.c.IdJeuIntegre',
                              backref="integrated")

    boardgameaccessories = relationship('Game',
                                        secondary=bg_accessory_table,
                                        secondaryjoin='BoardGameAccessory.id == EstAccessoire.c.IdAccessoire',
                                        primaryjoin='BoardGame.id == EstAccessoire.c.IdJeuSociete',
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
                            primaryjoin='VideoGame.id == Contenu.c.IdJeuContenant',
                            secondaryjoin='VideoGame.id == Contenu.c.IdJeuContenu',
                            backref="contained")

    adapts = relationship('BoardGame',
                          secondary=bg_vg_table,
                          primaryjoin='VideoGame.id == AdaptationJeuVideo.c.IdJeuVideo',
                          secondaryjoin='BoardGame.id == AdaptationJeuVideo.c.IdJeuPlateauAdapte',
                          backref="vgadaptation")

    expands = relationship('VideoGame',
                           secondary=expands_table,
                           primaryjoin='VideoGame.id == Extension.c.IdExtension',
                           secondaryjoin='VideoGame.id == Extension.c.IdJeuBase',
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

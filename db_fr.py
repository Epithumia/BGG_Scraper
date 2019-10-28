from sqlalchemy import Column, Integer, String, Float, Table
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

artist_table = Table('ArtisteJeu', Base.metadata,
                     Column('NumJeu', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                            primary_key=True),
                     Column('NumArtiste', Integer, ForeignKey('Personne.NumPersonne'), nullable=False,
                            primary_key=True))

designer_table = Table('DesignerJeu', Base.metadata,
                       Column('NumJeu', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                              primary_key=True),
                       Column('NumDesigner', Integer, ForeignKey('Personne.NumPersonne'), nullable=False,
                              primary_key=True))

publisher_table = Table('EditeurJeu', Base.metadata,
                        Column('NumJeu', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                               primary_key=True),
                        Column('NumEditeur', Integer, ForeignKey('Compagnie.NumCompagnie'), nullable=False,
                               primary_key=True))

mechanics_table = Table('MecaniqueJeu', Base.metadata,
                        Column('NumJeu', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                               primary_key=True),
                        Column('NumPropriete', Integer, ForeignKey('Propriete.NumPropriete'), nullable=False,
                               primary_key=True))

category_table = Table('CategorieJeu', Base.metadata,
                       Column('NumJeu', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                              primary_key=True),
                       Column('NumPropriete', Integer, ForeignKey('Propriete.NumPropriete'), nullable=False,
                              primary_key=True))

family_table = Table('FamilleJeu', Base.metadata,
                     Column('NumJeu', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                            primary_key=True),
                     Column('NumFamille', Integer, ForeignKey('Label.NumLabel'), nullable=False,
                            primary_key=True))

subdomain_table = Table('SousDomaineJeu', Base.metadata,
                        Column('NumJeu', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                               primary_key=True),
                        Column('NumSousDomaine', Integer, ForeignKey('Label.NumLabel'), nullable=False,
                               primary_key=True))

contains_table = Table('Contenu', Base.metadata,
                       Column('contains_id', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                              primary_key=True),
                       Column('contained_id', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                              primary_key=True))

reimplements_table = Table('Reimplementation', Base.metadata,
                           Column('NumJeuReimplementeur', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                                  primary_key=True),
                           Column('NumJeuReimplemente', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                                  primary_key=True))

expands_table = Table('Expansion', Base.metadata,
                      Column('NumExpansion', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                             primary_key=True),
                      Column('NumJeuExpanse', Integer, ForeignKey('Jeu.NumJeu'), nullable=False,
                             primary_key=True))


class Verbosity(Base):
    __tablename__ = 'DependanceLangue'

    id = Column(Integer, primary_key=True, name='NumDepLang', autoincrement=True)
    text = Column(String, nullable=False, name='LibelleDepLang')
    games = relationship("Game", back_populates="languagedependency")


class Company(Base):
    __tablename__ = 'Compagnie'

    id = Column(Integer, primary_key=True, name='NumCompagnie')
    name = Column(String, nullable=False, name='NomCompagnie')
    website = Column(String, name='SiteWebCompagnie')


class Person(Base):
    __tablename__ = 'Personne'

    id = Column(Integer, primary_key=True, name='NumPersonne')
    name = Column(String, nullable=False, name='NomPersonne')


class Property(Base):
    __tablename__ = 'Propriete'

    id = Column(Integer, primary_key=True, name='NumPropriete')
    name = Column(String, nullable=False, name='NomPropriete')
    type = Column('type', String(50))
    __mapper_args__ = {'polymorphic_on': type}


class Mechanic(Property):
    __mapper_args__ = {'polymorphic_identity': 'mecaniquejeu'}


class Category(Property):
    __mapper_args__ = {'polymorphic_identity': 'categoriejeu'}


class Label(Base):
    __tablename__ = 'Label'

    id = Column(Integer, primary_key=True, name='NumLabel')
    name = Column(String, nullable=False, name='NomLabel')
    subtype = Column(String, nullable=False, name='SousTypeLabel')
    __mapper_args__ = {'polymorphic_on': subtype}


class Family(Label):
    __mapper_args__ = {'polymorphic_identity': 'famille'}
    description = Column(String, name='Description')


class SubDomain(Label):
    __mapper_args__ = {'polymorphic_identity': 'sousdomaine'}


class Game(Base):
    __tablename__ = 'Jeu'

    id = Column(Integer, primary_key=True, name='NumJeu')
    name = Column(String, name='NomJeu')
    type = Column(String, nullable=False)
    yearpublished = Column(Integer, name='AnneePubliJeu')
    minplayers = Column(Integer, name='MinJouJeu')
    maxplayers = Column(Integer, name='MaxJouJeu')
    minplaytime = Column(Integer, name='MinDureeJeu')
    maxplaytime = Column(Integer, name='MaxDureeJeu')
    minage = Column(Integer, name='AgeMinJeu')
    rank = Column(Integer, name='RangJeu')
    average_rating = Column(Float, name='NoteMoyJeu')
    bayes_average_rating = Column(Float, name='NoteMoyPondJeu')
    best_minplayers = Column(Integer, name='MeilleurMinJouJeu')
    best_maxplayers = Column(Integer, name='MeilleurMaxJouJeu')
    recommended_minplayers = Column(Integer, name='MinJouRecomJeu')
    recommended_maxplayers = Column(Integer, name='MaxJouRecomJeu')
    recommended_age = Column(String, name='AgeRecomJeu')
    id_languagedependency = Column(Integer, ForeignKey(Verbosity.id))
    languagedependency = relationship(Verbosity, back_populates='games')
    artists = relationship(Person,
                           secondary=artist_table,
                           backref="games_art")
    designers = relationship(Person,
                             secondary=designer_table,
                             backref="games_design")
    publishers = relationship(Company,
                              secondary=publisher_table,
                              backref="games")
    categories = relationship(Category,
                              secondary=category_table,
                              backref="games_cat")
    mechanics = relationship(Mechanic,
                             secondary=mechanics_table,
                             backref="games_meca")
    families = relationship(Family,
                            secondary=family_table,
                            backref="games_fam")
    subdomains = relationship(SubDomain,
                              secondary=subdomain_table,
                              backref="games_sub")
    reimplements = relationship('Game',
                                secondary=reimplements_table,
                                primaryjoin=id == reimplements_table.c.NumJeuReimplementeur,
                                secondaryjoin=id == reimplements_table.c.NumJeuReimplemente,
                                backref="reimplemented")
    contains = relationship('Game',
                            secondary=contains_table,
                            primaryjoin=id == contains_table.c.contains_id,
                            secondaryjoin=id == contains_table.c.contained_id,
                            backref="contained")
    expands = relationship('Game',
                           secondary=expands_table,
                           primaryjoin=id == expands_table.c.NumExpansion,
                           secondaryjoin=id == expands_table.c.NumJeuExpanse,
                           backref="expanded")

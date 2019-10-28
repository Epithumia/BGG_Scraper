from sqlalchemy import Column, Integer, String, Float, Table
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

artist_table = Table('GameArtist', Base.metadata,
                     Column('game_id', Integer, ForeignKey('Game.id'), nullable=False, primary_key=True),
                     Column('artist_id', Integer, ForeignKey('Person.id'), nullable=False, primary_key=True))

designer_table = Table('GameDesigner', Base.metadata,
                       Column('game_id', Integer, ForeignKey('Game.id'), nullable=False, primary_key=True),
                       Column('designer_id', Integer, ForeignKey('Person.id'), nullable=False, primary_key=True))

publisher_table = Table('GamePublisher', Base.metadata,
                        Column('game_id', Integer, ForeignKey('Game.id'), nullable=False, primary_key=True),
                        Column('publisher_id', Integer, ForeignKey('Company.id'), nullable=False, primary_key=True))

mechanics_table = Table('GameMechanics', Base.metadata,
                        Column('game_id', Integer, ForeignKey('Game.id'), nullable=False, primary_key=True),
                        Column('property_id', Integer, ForeignKey('Property.id'), nullable=False, primary_key=True))

category_table = Table('GameCategory', Base.metadata,
                       Column('game_id', Integer, ForeignKey('Game.id'), nullable=False, primary_key=True),
                       Column('property_id', Integer, ForeignKey('Property.id'), nullable=False, primary_key=True))

family_table = Table('GameFamily', Base.metadata,
                     Column('game_id', Integer, ForeignKey('Game.id'), nullable=False,
                            primary_key=True),
                     Column('family_id', Integer, ForeignKey('Label.id'), nullable=False,
                            primary_key=True))

subdomain_table = Table('GameSubDomain', Base.metadata,
                        Column('game_id', Integer, ForeignKey('Game.id'), nullable=False,
                               primary_key=True),
                        Column('subdomain_id', Integer, ForeignKey('Label.id'), nullable=False,
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


class Verbosity(Base):
    __tablename__ = 'LanguageDependency'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    games = relationship("Game", back_populates="languagedependency")


class Company(Base):
    __tablename__ = 'Company'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    website = Column(String, name='SiteWebCompagnie')


class Person(Base):
    __tablename__ = 'Person'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Property(Base):
    __tablename__ = 'Property'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column('type', String(50))
    __mapper_args__ = {'polymorphic_on': type}


class Mechanic(Property):
    __mapper_args__ = {'polymorphic_identity': 'gamemechanic'}


class Category(Property):
    __mapper_args__ = {'polymorphic_identity': 'gamecategory'}


class Label(Base):
    __tablename__ = 'Label'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subtype = Column(String, nullable=False)
    __mapper_args__ = {'polymorphic_on': subtype}


class Family(Label):
    __mapper_args__ = {'polymorphic_identity': 'family'}
    description = Column(String, name='Description')


class SubDomain(Label):
    __mapper_args__ = {'polymorphic_identity': 'subdomain'}


class Game(Base):
    __tablename__ = 'Game'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    yearpublished = Column(Integer)
    minplayers = Column(Integer)
    maxplayers = Column(Integer)
    minplaytime = Column(Integer)
    maxplaytime = Column(Integer)
    minage = Column(Integer)
    rank = Column(Integer)
    average_rating = Column(Float)
    bayes_average_rating = Column(Float)
    best_minplayers = Column(Integer)
    best_maxplayers = Column(Integer)
    recommended_minplayers = Column(Integer)
    recommended_maxplayers = Column(Integer)
    recommended_age = Column(String)
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
                                primaryjoin=id == reimplements_table.c.reimplements_id,
                                secondaryjoin=id == reimplements_table.c.reimplemented_id,
                                backref="reimplemented")
    contains = relationship('Game',
                            secondary=contains_table,
                            primaryjoin=id == contains_table.c.contains_id,
                            secondaryjoin=id == contains_table.c.contained_id,
                            backref="contained")
    expands = relationship('Game',
                           secondary=expands_table,
                           primaryjoin=id == expands_table.c.expands_id,
                           secondaryjoin=id == expands_table.c.expanded_id,
                           backref="expanded")

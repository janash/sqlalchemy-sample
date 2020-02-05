"""
Table models for SQLAlchemy database.
"""

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Journal(Base):
    __tablename__ = 'journals'

    name = Column(String, primary_key=True)
    publisher = Column(String, nullable=True)
    papers = relationship('Paper', backref='journal')


class Paper(Base):
    __tablename__ = 'papers'

    DOI = Column(String, primary_key=True)
    paper_title = Column(String, nullable=False)
    publication_year = Column(Integer, nullable=False)

    journal_name = Column(String, ForeignKey('journals.name'))
    # First argument is class name for table, back populates

    def __str__(self):
        return F'Papers(DOI={self.DOI}, paper_title={self.paper_title})'

class Author(Base):
    __tablename__ = 'authors'

    name = Column(String, primary_key=True)
    affiliation = Column(String, nullable=True)

class Project(Base):
    __tablename__ = 'projects'

    name = Column(String, primary_key=True)
    description = Column(String, nullable=True)
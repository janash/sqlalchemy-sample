"""
Table models for SQLAlchemy database.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table

# one to many - journal to article
# many to one - author to paper or paper to project. Project may be easier to demonstrate

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
    authors = Column(String, nullable=False)

    journal_name = Column(String, ForeignKey('journals.name'))
    # First argument is class name for table, back populates

    def __str__(self):
        return F'Papers(DOI={self.DOI}, paper_title={self.paper_title})'


association_table = Table('project_papers', Base.metadata, 
    Column('project_name', String, ForeignKey('projects.name')),
    Column('paper_doi', String, ForeignKey('papers.DOI'))
)

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    papers = relationship("Paper", secondary=association_table, backref="projects")



"""
Table models for SQLAlchemy database.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()

class Paper(Base):
    __tablename__ = 'papers'

    DOI = Column(String, primary_key=True)
    paper_title = Column(String, nullable=False)
    journal = Column(String, nullable=False)
    publication_year = Column(Integer, nullable=False)
    authors = Column(String, nullable=False)

    def __str__(self):
        return F'Papers(DOI={self.DOI}, paper_title={self.paper_title})'
#    authors = relationship("PaperAuthors", back_populates="papers")
#    projects = relationship("ProjectPapers", back_populates="papers")

#class Authors(Base):
#    __tablename__ = 'authors'
#    authorID = Column(Integer, primary_key=True)
#    first_name = Column(String, nullable=False)
#    initials = Column(String, nullable=True)
#    last_name = Column(String, nullable=False)

#class PaperAuthors(Base):
#    __tablename__ = 'paper_authors'
#    
#    DOI = Column(String, ForeignKey('papers.DOI'), primary_key=True)
#    author = Column(String, ForeignKey('authors.authorID'), primary_key=True)

#class Projects(Base):
#    __tablename__ = 'projects'

#    name = Column(String, primary_key=True)
#    description = Column(String, nullable=True)

#class ProjectPapers(Base):
#    __tablename__ = 'project_papers'

#    project_name = Column(String, ForeignKey('projects.name'), primary_key=True)
#    project_papers = Column(String, ForeignKey('papers.DOI'), primary_key=True)


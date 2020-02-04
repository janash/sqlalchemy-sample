"""
Table models for SQLAlchemy database.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

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

    journal_id = Column(String, ForeignKey('journals.name'))
    # First argument is class name for table, back populates

    def __str__(self):
        return F'Papers(DOI={self.DOI}, paper_title={self.paper_title})'


#class Projects(Base):
#    __tablename__ = 'projects'

#    name = Column(String, primary_key=True)
#    description = Column(String, nullable=True)

#class ProjectPapers(Base):
#    __tablename__ = 'project_papers'

#    project_name = Column(String, ForeignKey('projects.name'), primary_key=True)
#    project_papers = Column(String, ForeignKey('papers.DOI'), primary_key=True)


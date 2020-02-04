"""
Make and manipulate the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Papers

engine = create_engine('sqlite:///my_papers.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

# Add some papers to the DB
my_paper = Papers(DOI='10.1063/1.5052551', paper_title='Perspective: Computational chemistry software and its advancement as illustrated through three grand challenge cases for molecular science', journal='J. Chem. Phys', publication_year=2018, authors='Anna Krylov, Theresa L. Windus, Taylor Barnes, Eliseo Marin-Rimoldi, Jessica A. Nash')

session.add(my_paper)
session.commit()

session.close()
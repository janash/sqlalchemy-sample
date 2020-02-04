"""
Make and manipulate the database
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Papers

os.remove('my_papers.db')

engine = create_engine('sqlite:///my_papers.db')
Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)

# Add a paper to the DB
molssi_paper = Papers(DOI='10.1063/1.5052551', paper_title='Perspective: Computational chemistry software and its advancement as illustrated through three grand challenge cases for molecular science', journal='J. Chem. Phys', publication_year=2018, authors='Anna Krylov, Theresa L. Windus, Taylor Barnes, Eliseo Marin-Rimoldi, Jessica A. Nash')

session.add(molssi_paper)
session.commit()

# Retrieve from DB
print(session.query(Papers).one())

session.close()
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
molssi_paper = Papers(DOI='10.1063/1.5052551', paper_title='Perspective: Computational chemistry software and its advancement as illustrated through three grand challenge cases for molecular science', journal='J. Chem. Phys', publication_year=2018, authors='Anna Krylov, Theresa L. Windus, Taylor Barnes, Eliseo Marin-Rimoldi, Jessica A. Nash, Benjamin Pritchard, Daniel G.A. Smith, Doaa Altarawy, Paul Saxe, Cecilia Clementi, T. Daniel Crawford, Robert J. Harrison, Shantenu Jha, Vijay S. Pande, Teresa Head-Gordon')

# Add another paper
bse_paper = Papers(DOI='10.1021/acs.jcim.9b00725', paper_title='New Basis Set Exchange: An Open, Up-to-Date Resource for the Molecular Sciences Community', journal='J Chem. Inf. Model', publication_year=2019, authors='Benjamin P. Pritchard, Doaa Altarawy, Brett Didier, Tara D. Gibson, Theresa L. Windus')

session.add(molssi_paper)
session.add(bse_paper)
session.commit()

# Retrieve from DB
#my_paper = session.query(Papers).first()
#print(my_paper.paper_title)

all_papers = session.query(Papers).all()

for paper in all_papers:
    print(F'{paper.DOI} \t {paper.paper_title}')

session.close()
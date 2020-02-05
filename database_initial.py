"""
Make and manipulate the database
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models_initial import Base, Paper, Journal, Project

if os.path.isfile('my_papers.db'):
    os.remove('my_papers.db')
    
# echo true goes on engine
engine = create_engine('sqlite:///my_papers.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

jchem_phys = Journal(name='J. Chem. Phys', publisher='AIP')

# Add another paper
bse_paper = Paper(DOI='10.1021/acs.jcim.9b00725', paper_title='New Basis Set Exchange: An Open, Up-to-Date Resource for the Molecular Sciences Community', publication_year=2019, journal_name='J. Chem. Inf. Model')

# Add another paper for J Chem Phys
crawford_paper = Paper(DOI='10.1063/1.2137323', paper_title='Sources of error in electronic structure calculations on small chemical systems', publication_year=2006)

molssi_paper = Paper(DOI='10.1063/1.5052551', paper_title='Perspective: Computational chemistry software and its advancement as illustrated through three grand challenge cases for molecular science', publication_year=2018, journal_name="J. Chem. Phys.")

session.add(molssi_paper)

#session.add(jcim)

session.commit()

session.close()
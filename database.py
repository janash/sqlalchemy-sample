"""
Make and manipulate the database
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Paper

try:
    os.remove('my_papers.db')
except:
    pass

# echo true goes on engine
engine = create_engine('sqlite:///my_papers.db')
Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)

# Add a paper to the DB
molssi_paper = Paper(DOI='10.1063/1.5052551', paper_title='Perspective: Computational chemistry software and its advancement as illustrated through three grand challenge cases for molecular science', journal='J. Chem. Phys', publication_year=2018, authors='Anna Krylov, Theresa L. Windus, Taylor Barnes, Eliseo Marin-Rimoldi, Jessica A. Nash, Benjamin Pritchard, Daniel G.A. Smith, Doaa Altarawy, Paul Saxe, Cecilia Clementi, T. Daniel Crawford, Robert J. Harrison, Shantenu Jha, Vijay S. Pande, Teresa Head-Gordon')

# Add another paper
bse_paper = Paper(DOI='10.1021/acs.jcim.9b00725', paper_title='New Basis Set Exchange: An Open, Up-to-Date Resource for the Molecular Sciences Community', journal='J Chem. Inf. Model', publication_year=2019, authors='Benjamin P. Pritchard, Doaa Altarawy, Brett Didier, Tara D. Gibson, Theresa L. Windus')

session.add(molssi_paper)
session.add(bse_paper)
session.commit()

# Retrieve from DB
#my_paper = session.query(Papers).first()
#print(my_paper.paper_title)

all_papers = session.query(Paper).all()
#for paper in all_papers:
#    print(F'{paper.DOI} \t {paper.paper_title}')

# What if we wanted to find all papers Ben was an author on?
# We COULD do this, but this could create problems if we ever had
# two authors with the same name. Instead, we can create another 
# table of authors, where each author has an ID.
ben_papers = session.query(Paper).filter(Paper.authors.contains('Jessica'))

author_list1 = 'Anna Krylov, Theresa L. Windus, Taylor Barnes, Eliseo Marin-Rimoldi, Jessica A. Nash, Benjamin Pritchard, Daniel G.A. Smith, Doaa Altarawy, Paul Saxe, Cecilia Clementi, T. Daniel Crawford, Robert J. Harrison, Shantenu Jha, Vijay S. Pande, Teresa Head-Gordon'

# Note that this script is very specific to our use case.
for author in author_list1.split(','):
    split_name = author.split()

    first_name = split_name[0]
    if len(split_name) > 2:
        last_name= split_name[2:]
        initial = split_name[1]
    elif len(split_name) == 2:
        last_name = split_name[1]
        initial = None
    
    #add_author = Author(first_name=first_name, initial=initial, last_name=last_name)
    #session.add(add_author)


session.commit()

        

for paper in ben_papers:
    print(paper.paper_title)

session.close()
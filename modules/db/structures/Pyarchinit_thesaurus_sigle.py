'''
Created on 19 feb 2018

@author: Serena Sensini
'''

from modules.db.pyarchinit_conn_strings import Connection
from sqlalchemy import Table, Column, Integer, Date, String, Text, Float, Numeric, MetaData, ForeignKey, engine, create_engine, UniqueConstraint


class Pyarchinit_thesaurus_sigle:
    # connection string postgres"
    internal_connection = Connection()

    # create engine and metadata

    engine = create_engine(internal_connection.conn_str(), echo=False, convert_unicode = True)
    metadata = MetaData(engine)

    # define tables
    pyarchinit_thesaurus_sigle = Table('pyarchinit_thesaurus_sigle', metadata,
    Column('id_thesaurus_sigle', Integer, primary_key=True),
    Column('nome_tabella', Text),
    Column('sigla', String(3)),
    Column('sigla_estesa', Text),
    Column('descrizione', Text),
    Column('tipologia_sigla', Text),

    # explicit/composite unique constraint.  'name' is optional.
    UniqueConstraint('id_thesaurus_sigle', name='id_thesaurus_sigle_pk')
    )

    metadata.create_all(engine)
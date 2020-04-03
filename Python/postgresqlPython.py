# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Grava registros armazenados em um DataFrame no banco de dados PostgreSQL. ---

import pandas as pd
from sqlalchemy import create_engine

df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})
engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
df.to_sql('table_name', engine)
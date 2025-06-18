# ---------------------------------------------------------------------------------------------
# Trabalahndo com banco de dados SQLite

import sqlite3

conexao = sqlite3.connect('aula36.db')
c = conexao.cursor()

# c.execute('CREATE TABLE IF NOT EXISTS usuario(id integer, nome text)')
# c.execute('INSERT INTO usuario VALUES(1, "Joao")')
# c.execute('INSERT INTO usuario VALUES(2, "Rodrigo")')
# c.execute('INSERT INTO usuario VALUES(3, "Maria")')

# conexao.commit()

requisicao = 'SELECT * FROM usuario WHERE nome = ?'
for linha in c.execute(requisicao, ('Maria',)):
    print(linha)

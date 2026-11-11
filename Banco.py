import sqlite3
import seguranca

def criar_tabela():
    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        senha_hash TEXT NOT NULL,
        criado_em TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        token_hash TEXT NOT NULL UNIQUE,
        expira_em TEXT NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )
    """)

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS  lista_compras(
    
    id_lista INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_lista TEXT NOT NULL,
    usuario_id INTEGER NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)

    )
""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS itens_lista (
        id_item INTEGER PRIMARY KEY AUTOINCREMENT,
        id_lista INTEGER NOT NULL,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        FOREIGN KEY (id_lista) REFERENCES lista_compras(id_lista)
    )
""")
    conexao.commit()
    conexao.close()

def salvar_usuario(nome, cpf, email, senha_hash):
    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nome, cpf, email, senha_hash)
        VALUES (?, ?, ?, ?)
    """, (nome, cpf, email, senha_hash))

    conexao.commit()
    conexao.close()

def email_ja_cadastrado(email):

    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute(""" SELECT id FROM usuarios WHERE email = ? """,(email,))

    resultado = cursor.fetchone()

    conexao.close()

    return resultado is not None

def cpf_ja_cadastrado(cpf):

    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute("""SELECT id FROM usuarios WHERE cpf = ? """,(cpf,))

    resultado = cursor.fetchone()

    conexao.close()

    return resultado is not None

def senha_certa(email, senha):
    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT senha_hash FROM usuarios WHERE email = ?",
        (email,)
    )

    resultado = cursor.fetchone()
    conexao.close()

    if resultado is None:
        return False

    senha_salva = resultado[0]

    return seguranca.verificar_senha(senha, senha_salva)

def buscar_id_usuario(email):

    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute(""" SELECT id FROM usuarios WHERE email = ? """,(email,))

    resultado = cursor.fetchone()

    conexao.close()

    if resultado is None:
        return None

    return resultado[0]

def salvar_sessao(usuario_id, token_hash, expira_em):
    conexao = sqlite3.connect("banco_dados.db")
    conexao.execute("PRAGMA foreign_keys = ON")

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO sessoes (usuario_id, token_hash, expira_em)
        VALUES (?, ?, ?)
    """, (usuario_id, token_hash, expira_em))

    conexao.commit()
    conexao.close()

def buscar_usuario_sessao_valida(token_hash):
    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT usuario_id
        FROM sessoes
        WHERE token_hash = ?
          AND datetime(expira_em) > datetime('now')
    """, (token_hash,))

    resultado = cursor.fetchone()

    conexao.close()

    if resultado is None:
        return None

    return resultado[0]

def Buscar_usuario_ativo(id):

    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT nome,cpf,email FROM usuarios WHERE id = ?",
        (id,)
    )

    resultado = cursor.fetchone()

    conexao.close()

    if resultado:
        return id, resultado[0],resultado[1],resultado[2]
    else:
        return None

def excluir_sessao(token_hash):

    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute(
    "DELETE FROM sessoes WHERE token_hash = ?",
    (token_hash,)
    )

    conexao.commit()
    conexao.close()

def get_id_lista(nome_lista,usuario_id):

    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute("""SELECT id_lista FROM lista_compras WHERE nome_lista = ? AND usuario_id = ? """,(nome_lista,usuario_id))

    resultado = cursor.fetchone()

    if resultado is None:
        return None

    conexao.commit()
    conexao.close()

    return resultado[0]

def Criar_lista(usuario_id,nome_lista):

    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO lista_compras (usuario_id,nome_lista) VALUES(?,?)",
        (usuario_id,nome_lista)
    )
    id_list = cursor.lastrowid

    conexao.commit()
    conexao.close()

    return id_list

def Salvar_item(id_lista,produto,quantidade):

    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO itens_lista(id_lista,produto,quantidade) VALUES(?,?,?)",
        (id_lista,produto,quantidade)
    )

    conexao.commit()
    conexao.close()

def Acessar_todas_listas(usuario_id):

    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id_lista,nome_lista FROM lista_compras WHERE usuario_id = ?",
        (usuario_id,)
    )

    listas = cursor.fetchall()

    conexao.commit()
    conexao.close()

    return listas 

def apagar_todas_listas():
    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM itens_lista")
    cursor.execute("DELETE FROM lista_compras")

    conexao.commit()
    conexao.close()

def itens_da_lista(id_lista):

    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute(
    "SELECT produto, quantidade FROM itens_lista WHERE id_lista = ?",
    (id_lista,)
)
    itens = cursor.fetchall()

    conexao.commit()
    conexao.close()

    return itens

def Apagar_lista(id_lista):

    conexao = sqlite3.connect("banco_dados.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM itens_lista WHERE id_lista = ?",(id_lista,))
    cursor.execute("DELETE FROM lista_compras WHERE id_lista = ?",(id_lista,))

    conexao.commit()
    conexao.close()

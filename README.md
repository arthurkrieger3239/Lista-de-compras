# Lista de compras

Meu primeiro projeto pessoal: um aplicativo de gerenciamento de compras e gastos feito com **Python, Flet e SQLite**.

> Em desenvolvimento. A tela inicial utiliza dados de demonstração; as funcionalidades de compras, listas e histórico ainda estão sendo implementadas.

## Bibliotecas necessárias

- **Flet:** interface gráfica.
- **python-dotenv:** leitura das configurações do arquivo `.env`.
- **email-validator:** validação de e-mail.
- **argon2-cffi:** hash e verificação de senhas.
- **cryptography:** criptografia dos tokens de sessão.

Com o Python instalado, execute no terminal para instalar todas:

```powershell
python -m pip install "flet[desktop]==0.86.5" python-dotenv email-validator argon2-cffi cryptography
```

O SQLite já acompanha o Python.

## Como abrir

Abra o terminal na pasta do projeto, onde está o arquivo `main.py`, e execute:

```powershell
python main.py
```

=======
Para usar a opção **Lembrar de mim**, configure a variável `LISTA_COMPRAS_SECRET_KEY` no arquivo `.env` local. 


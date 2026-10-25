
# Lista de compras

Aplicativo de gerenciamento de compras e gastos desenvolvido com **Python, Flet e SQLite**.

Este é meu primeiro projeto pessoal. Estou construindo a aplicação para praticar desenvolvimento de interfaces, organização do código, autenticação e persistência de dados, com o objetivo de facilitar o acompanhamento de compras e despesas do dia a dia.

> **Em desenvolvimento:** as telas de cadastro, login e início já foram construídas. A tela inicial utiliza dados de demonstração; as funcionalidades de compras, listas e histórico ainda estão sendo implementadas.

## O que já foi desenvolvido

- Telas de cadastro e login, com componentes visuais reutilizáveis.
- Validação de nome, CPF, e-mail, senha e confirmação de senha no cadastro.
- Rotinas de cadastro e verificação de credenciais com SQLite.
- Armazenamento de senhas com hash Argon2.
- Rotinas para manter a sessão com a opção **Lembrar de mim**, incluindo expiração, hash do token no banco e criptografia do token armazenado localmente.
- Tela inicial com cabeçalho, resumo de gastos, ações de compra, lista de compras, compras recentes e menu inferior.
- Layout da tela inicial adaptável à largura da janela, com rolagem vertical e menu inferior fora da área rolável.
- Separação entre interface, controles, modelos, navegação e validações.

## Próximas etapas

- [ ] Concluir a integração dos dados do usuário entre login e tela inicial.
- [ ] Implementar o cadastro de compras, itens e valores.
- [ ] Criar e atualizar listas de compras.
- [ ] Disponibilizar histórico e detalhes das compras.
- [ ] Substituir os dados de demonstração por consultas ao banco.
- [ ] Conectar o resumo de gastos e orçamento aos dados reais.
- [ ] Implementar as ações de perfil, recuperação de senha e navegação das demais seções.
- [ ] Ampliar os testes dos fluxos e validar a interface em dispositivos móveis.

Atualmente, algumas ações dos botões ainda não possuem implementação. As rotinas de conta e sessão também estão em fase de integração; o fluxo completo de uso ainda não está concluído.

## Tecnologias

| Tecnologia | Uso no projeto |
| --- | --- |
| Python | Lógica da aplicação e organização dos módulos |
| [Flet](https://flet.dev/) | Interface gráfica e eventos |
| SQLite | Armazenamento local de usuários e sessões |
| [argon2-cffi](https://argon2-cffi.readthedocs.io/) | Hash e verificação de senhas |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Carregamento das variáveis do arquivo `.env` |
| [email-validator](https://github.com/JoshData/python-email-validator) | Validação de e-mail |
| [cryptography](https://cryptography.io/) e `flet.security` | Proteção dos tokens de sessão |

Ambiente utilizado no desenvolvimento: **Windows, Python 3.14 e Flet 0.86.5**.

## Como executar

As instruções abaixo são para Windows com PowerShell e Python instalado.

### 1. Clonar o repositório

```powershell
git clone https://github.com/arthurkrieger3239/Lista-de-compras.git
cd Lista-de-compras
```

### 2. Criar um ambiente virtual

```powershell
python -m venv .venv
```

Os próximos comandos usam diretamente o Python desse ambiente virtual.

### 3. Instalar as dependências

```powershell
.\.venv\Scripts\python.exe -m pip install "flet[desktop]==0.86.5" python-dotenv email-validator argon2-cffi cryptography
```

O SQLite faz parte da biblioteca padrão do Python e não precisa ser instalado com `pip`.

### 4. Configurar a chave local de sessão

Em uma instalação nova, gere uma chave para a criptografia dos tokens:

```powershell
.\.venv\Scripts\python.exe -c "import secrets; print(secrets.token_urlsafe(32))"
```

Crie um arquivo chamado `.env` na raiz do projeto, ao lado de `main.py`, e coloque a chave gerada:

```dotenv
PROJETO_WILLIAM_SECRET_KEY=cole_aqui_a_chave_gerada
```

Se o ambiente já possui uma chave configurada, preserve a chave existente para permitir a leitura das sessões salvas. O arquivo `.env` é local e não deve ser enviado ao repositório.

### 5. Iniciar a aplicação

Execute o comando a partir da raiz do projeto:

```powershell
.\.venv\Scripts\python.exe main.py
```

As tabelas de usuários e sessões são criadas automaticamente no arquivo local `banco_dados.db` ao iniciar. Para usar a aplicação em uma instalação nova, comece pela tela de cadastro. Os dados de usuários e sessões ficam no banco local; os cards de compras e gastos ainda utilizam valores de demonstração.

## Estrutura do projeto

```text
Lista-de-compras/
├── Assets/              # Logo e fontes
├── Controles/           # Ações e fluxos das telas
├── Modelos/             # Classes de usuário
├── Navegacao/           # Configuração da página e troca de telas
├── Telas/               # Login, cadastro, início e componentes reutilizáveis
├── Verificacoes/        # Validação dos dados de cadastro
├── Banco.py             # Criação das tabelas e operações SQLite
├── main.py              # Ponto de entrada da aplicação
├── seguranca.py         # Hash de senhas e tokens
└── README.md
```

O `.env`, o ambiente virtual e o banco com os dados locais ficam fora do versionamento.

## Aprendizados

Durante o desenvolvimento, estou praticando:

- Construção de interfaces e tratamento de eventos com Flet.
- Organização de um projeto Python em módulos com responsabilidades diferentes.
- Consultas e persistência de dados com SQLite.
- Validação de formulários e tratamento de credenciais e sessões.
- Adaptação de layouts a diferentes tamanhos de janela.
- Uso de Git e GitHub para acompanhar a evolução do projeto.

## Autor

Desenvolvido por Arthur Krieger(https://github.com/arthurkrieger3239).

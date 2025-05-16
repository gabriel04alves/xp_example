# SIGAA Token API

**Projeto de estudos para a atividade individual da disciplina Engenharia de Software I**, curso de Bacharelado em Sistemas de Informação no Instituto Federal Catarinense – Campus Araquari.

Este repositório contém uma **API simples em FastAPI** que simula autenticação via JWT, desenvolvida como exercício de **Extreme Programming (XP)**, com foco em resolver o problema de **expiração rápida de tokens** em sistemas de gestão acadêmica (ex: SIGAA).

## Objetivo da Atividade

1. **TDD (Test-Driven Development)**: escrever testes antes da implementação.
2. **Autenticação**: criar endpoint de login que gera token JWT.
3. **Refatoração mínima**: código limpo e modular (separação em `auth.py` e `main.py`).
4. **Aplicar práticas de XP**: utilizar metodologia ágil Extreme Programming.

5. **Resolver problema real**: demonstrar como lidar com tokens de expiração baixa.

## Funcionalidades Entregues

- **Quadro Kanban** no GitHub Projects para acompanhar tarefas: [GitHub Projects](https://github.com/users/gabriel04alves/projects/2).
- `POST /token`: gera um JWT com expiração de **24 horas**.
- **Testes automatizados** via **pytest** e **httpx**, garantindo TDD para o endpoint de autenticação.
- Projeto organizado conforme **git flow**: branch `dev` para desenvolvimento e `master` para produção.
- **Commits semânticos** seguindo Conventional Commits.

## Tecnologias Utilizadas

- FastAPI
- Python-JOSE para JWT
- pytest + httpx para testes
- uvicorn como servidor ASGI

## Estrutura do Projeto

```
sigaa_token_api/
├── main.py        # Definição do endpoint /token
├── auth.py        # Lógica de criação de JWT
├── test_main.py   # Testes TDD para o endpoint de login
├── README.md      # Documentação do projeto
└── .gitignore     # Arquivos ignorados pelo Git
```

## Como Rodar Localmente

1. **Clone** o repositório:

   ```bash
   git clone https://github.com/gabriel04alves/sigaa-token-api.git
   cd sigaa-token-api
   ```

2. **Virtualenv**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
   ```

3. **Dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Testes**:

   ```bash
   pytest
   ```

5. **Iniciar API**:
   ```bash
   uvicorn main:app --reload
   ```

## Licença

MIT License

# Desafio Técnico - API de Controle de Visitantes em Condomínios

---

## 🎯 Objetivo

Desenvolver uma **API RESTful** para gerenciar o **fluxo de entrada e saída de visitantes** em condomínios.

---

## 📝 Requisitos

A API oferece recursos para gerenciar:

* **Visitantes**: Cadastro, listagem, atualização e remoção.
* **Condomínios e Unidades**: Listagem de condomínios e suas unidades, incluindo a relação entre eles.
* **Controle de Acesso**: Liberação de entrada, baixa de saída e listagem de movimentações por unidade.

---

## ⚙️ Tecnologias e Requisitos Técnicos

* **Linguagem**: Python
* **Framework Web**: FastAPI
* **Banco de Dados**: SQLite
* **ORM**: SQLAlchemy
* **Documentação**: Swagger/OpenAPI
* **Controle de Versão**: Git

---

## 🚀 Como Rodar o Projeto

Siga estes passos simples para configurar e executar a API.

### Pré-requisitos

* Python 3.8+
* Git

### Instalação e Execução

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/ViniciusAugustoJesus/Desafio-Controle-Visitantes-Condominio.git
    cd controle_visitantes
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    # Se ainda não tiver o requirements.txt, crie com:
    # pip freeze > requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    uvicorn app.main:app --reload
    ```
    A API estará disponível em `http://127.0.0.1:8000`.

---

## 📖 Documentação da API

A documentação interativa (Swagger UI) está disponível em:
[http://127.0.0.1:8000/docs]

Use esta interface para explorar os endpoints, visualizar esquemas e testar as funcionalidades da API.

---

## 📁 Estrutura do Projeto
controle_visitantes/
├── venv/
├── app/
│   ├── main.py            # Ponto de entrada da API
│   ├── database.py        # Configuração do DB e SQLAlchemy
│   ├── models.py          # Modelos do banco de dados
│   ├── schemas.py         # Schemas Pydantic para validação
│   ├── crud.py            # Operações CRUD
│   └── routers/           # Módulos de rotas (visitantes, condominios, controle_acesso)
├── .gitignore
├── README.md
├── requirements.txt

## ✉️ Observações

* O banco de dados SQLite (`sql_app.db`) será criado automaticamente na primeira execução e populado com dados iniciais para facilitar os testes.
* Priorize a lógica, organização e clareza do código. Entregue o que conseguir e utilize este README para explicar o que foi feito e o que ficou pendente, se for o caso.
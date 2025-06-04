# API de Controle de Visitantes em Condomínios

Esta aplicação é uma API RESTful desenvolvida em FastAPI para gerenciar o fluxo de entrada e saída de visitantes em condomínios. Utiliza SQLAlchemy para ORM e SQLite como banco de dados padrão.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/ViniciusAugustoJesus/Desafio-Controle-Visitantes-Condominio.git
   cd controle_visitantes
   ```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   # Ative o ambiente:
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```bash
   uvicorn app.main:app --reload
   ```

Acesse a documentação interativa em [http://localhost:8000/docs](http://localhost:8000/docs)

## Principais Rotas

### Visitantes
- `POST /visitantes/` — Cadastra um novo visitante
- `GET /visitantes/` — Lista todos os visitantes
- `GET /visitantes/{visitante_id}` — Detalha um visitante
- `PUT /visitantes/{visitante_id}` — Atualiza um visitante
- `DELETE /visitantes/{visitante_id}` — Remove um visitante

### Condomínios e Unidades
- `POST /condominios/` — Cadastra um novo condomínio
- `GET /condominios/` — Lista todos os condomínios
- `GET /condominios/{condominio_id}` — Detalha um condomínio
- `GET /condominios/{condominio_id}/unidades` — Lista unidades de um condomínio
- `POST /condominios/{condominio_id}/unidades/` — Cadastra unidade em um condomínio
- `GET /condominios/relacao/unidades` — Lista condomínios com suas unidades

### Controle de Acesso
- `POST /controle-acesso/entrada` — Libera entrada de visitante
- `PUT /controle-acesso/saida/{movimentacao_id}` — Registra saída de visitante
- `GET /controle-acesso/unidades/{unidade_id}/movimentacoes` — Lista movimentações de uma unidade

## Dependências
- fastapi
- uvicorn
- sqlalchemy
- pydantic

## Banco de Dados
O projeto utiliza SQLite por padrão (arquivo `test.db`).

---

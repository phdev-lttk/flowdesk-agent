# 🤖 FlowDesk Agent — RAG com IA

Agente de Inteligência Artificial capaz de responder perguntas utilizando informações presentes em documentos PDF.

O projeto utiliza **RAG (Retrieval-Augmented Generation)** para buscar informações relevantes no documento e utilizá-las como contexto para gerar respostas claras e relacionadas à base de conhecimento.

> Projeto desenvolvido como atividade do programa **Oracle Next Education (ONE)**.

---

## 📸 Funcionamento

![FlowDesk Agent](./docs/flowdesk-agent.png)

O usuário envia uma pergunta através da interface de chat e o agente procura a informação correspondente na documentação da **FlowDesk**.

### Exemplo

**Pergunta:**

> Quais os planos disponíveis?

**Resposta:**

> Os planos disponíveis são: Gratuito, Básico e Profissional.

Caso uma informação não esteja presente no documento:

**Pergunta:**

> Qual o endereço da empresa?

**Resposta:**

> Essa informação não foi encontrada no documento.

Isso reduz respostas inventadas pelo modelo e mantém o agente baseado na fonte fornecida.

---

## 🧠 Como funciona o RAG

O fluxo da aplicação funciona da seguinte forma:

```text
PDF
 ↓
Extração do texto
 ↓
Divisão em trechos (chunks)
 ↓
Criação dos embeddings
 ↓
Indexação dos documentos
 ↓
Pergunta do usuário
 ↓
Busca semântica
 ↓
Recuperação dos trechos relevantes
 ↓
LLM recebe contexto + pergunta
 ↓
Resposta
```

Em vez de depender apenas do conhecimento do modelo de IA, o sistema recupera informações da documentação antes de gerar a resposta.

---

## 💬 Interações

Além das perguntas sobre os documentos, o agente consegue lidar com interações simples do cotidiano:

```text
Oi
Olá
Bom dia
Obrigado
Tchau
```

Perguntas relacionadas à documentação utilizam o fluxo RAG.

---

## 🛠️ Tecnologias

### Backend

* Python
* FastAPI
* Uvicorn
* PyMuPDF
* RAG
* Embeddings
* LLM

### Frontend

* React
* JavaScript
* Tailwind CSS

---

## 🏗️ Arquitetura

```text
┌─────────────┐
│   Usuário   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    React    │
│  Frontend   │
└──────┬──────┘
       │ HTTP
       ▼
┌─────────────┐
│   FastAPI   │
│   Backend   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│     RAG     │
└──────┬──────┘
       │
   ┌───┴────┐
   ▼        ▼
  PDF      LLM
```

---

## 📂 Estrutura

```text
projeto/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── documents/
│       └── flow_TOS.pdf
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── .gitignore
├── .env.example
└── README.md
```

---

## 🚀 Executando localmente

Clone o projeto:

```bash
git clone URL_DO_REPOSITORIO
cd NOME_DO_REPOSITORIO
```

### Backend

Entre na pasta:

```bash
cd backend
```

Crie o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure as variáveis de ambiente:

```env
API_KEY=sua_chave_aqui
```

Inicie a API:

```bash
uvicorn main:app --reload
```

O backend estará disponível em:

```text
http://127.0.0.1:8000
```

A documentação do FastAPI estará em:

```text
http://127.0.0.1:8000/docs
```

### Frontend

Em outro terminal:

```bash
cd frontend
npm install
npm run dev
```

Acesse a URL exibida pelo Vite no terminal.

---

## 📡 API

O frontend envia as perguntas para:

```http
POST /ask
```

Exemplo:

```json
{
  "question": "Quais os planos disponíveis?"
}
```

Resposta:

```json
{
  "answer": "Os planos disponíveis são: Gratuito, Básico e Profissional."
}
```

---

## 🧪 Exemplos para testar

Perguntas que possuem resposta na documentação:

```text
Quais os planos disponíveis?

Qual plano possui acesso à API?

Quantos usuários posso ter no plano gratuito?

Como recuperar minha senha?

Qual o tamanho máximo de um arquivo?

Posso cancelar minha assinatura?
```

Também é possível testar perguntas cuja informação não existe:

```text
Qual o endereço da empresa?

A FlowDesk possui aplicativo para smartwatch?
```

Nesses casos, o agente deve informar que não encontrou a informação na documentação.


---

## 🎓 Projeto

Projeto desenvolvido para o programa **Oracle Next Education (ONE)** com o objetivo de aplicar conceitos de:

**Inteligência Artificial • RAG • Python • FastAPI • React • Processamento de documentos • Cloud**

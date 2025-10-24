# 🤖 Agente Básico com Agno

Um projeto de exemplo demonstrando como criar um agente básico usando o framework [Agno](https://docs.agno.com/).

## 📋 O Que É Este Projeto?

Este é um agente conversacional simples que:

- ✅ Usa **Claude Sonnet 4** da Anthropic
- ✅ Tem **memória persistente** em SQLite
- ✅ Acessa a **documentação do Agno** via MCP
- ✅ Roda localmente com **privacidade total**
- ✅ Tem interface web via **AgentOS**

## 🚀 Como Começar

### 1. Pré-requisitos

- Python 3.10 ou superior
- Chave API da Anthropic ([obtenha aqui](https://console.anthropic.com/))

### 2. Instalação

```bash
# Clone ou baixe este projeto
cd agno_agent_reslmidor

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configuração

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env e adicione sua chave API
# ANTHROPIC_API_KEY=sk-ant-sua-chave-aqui
```

### 4. Executar

```bash
# Rode o agente
python agente_basico.py
```

Acesse em: **http://localhost:7777**

## 🎯 Como Usar

1. Abra seu navegador em `http://localhost:7777`
2. Você verá a interface do AgentOS
3. Comece a conversar com o agente!
4. O histórico é salvo automaticamente

### Exemplos de Perguntas

```
"Olá! Como você funciona?"
"Quais são suas capacidades?"
"Me explique o que é o Agno"
"Como posso criar meu próprio agente?"
```

## 📁 Estrutura do Projeto

```
agno_agent_reslmidor/
├── CLAUDE.md              # Documentação para Claude Code
├── README.md              # Este arquivo
├── requirements.txt       # Dependências Python
├── .env.example          # Template de configuração
├── .gitignore            # Arquivos ignorados pelo git
├── agente_basico.py      # Código principal do agente
└── agente.db             # Database SQLite (gerado automaticamente)
```

## 🧠 Arquitetura

```
┌─────────────────────────────────────────┐
│          Navegador Web                  │
│     http://localhost:7777               │
└─────────────────┬───────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────┐
│           AgentOS (FastAPI)             │
│  • Runtime de produção                  │
│  • Interface web integrada              │
│  • API REST                             │
└─────────────────┬───────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────┐
│        Agente Básico (Agno)             │
│  • Model: Claude Sonnet 4               │
│  • Memory: SQLite                       │
│  • Tools: MCP (docs.agno.com)           │
└─────────────────────────────────────────┘
```

## 🔧 Customização

### Adicionar Ferramentas

Edite `agente_basico.py` e adicione mais ferramentas:

```python
from agno.tools.duckduckgo import DuckDuckGo
from agno.tools.python import PythonTools

tools=[
    MCPTools(...),
    DuckDuckGo(),      # Busca na web
    PythonTools(),     # Executar código Python
]
```

### Mudar o Modelo

```python
# OpenAI GPT-4
from agno.models.openai import OpenAIChat
model=OpenAIChat(id="gpt-4")

# Google Gemini
from agno.models.google import Gemini
model=Gemini(id="gemini-pro")
```

### Adicionar Memória de Usuário

```python
from agno.memory.db import MemoryDb

agent = Agent(
    ...,
    memory=MemoryDb(db=db),  # Memória persistente
    add_memory_to_context=True,
)
```

## 📚 Recursos

- **Docs Agno**: https://docs.agno.com/
- **GitHub Agno**: https://github.com/agno-agi/agno
- **Cookbook**: https://github.com/agno-agi/agno/tree/main/cookbook
- **Anthropic API**: https://docs.anthropic.com/

## 🐛 Troubleshooting

### Erro: `ANTHROPIC_API_KEY não encontrada`

Certifique-se de:
1. Criar arquivo `.env` a partir de `.env.example`
2. Adicionar sua chave API válida
3. A chave começa com `sk-ant-`

### Erro: `ModuleNotFoundError: No module named 'agno'`

```bash
# Verifique se o ambiente virtual está ativo
# Reinstale as dependências
pip install -r requirements.txt
```

### Porta 7777 em uso

Edite `agente_basico.py` e mude a porta:

```python
agent_os.serve(
    ...,
    port=8888,  # Use outra porta
)
```

## 🤝 Contribuindo

Este é um projeto de aprendizado! Sinta-se livre para:

- Fazer fork e experimentar
- Adicionar novos recursos
- Melhorar a documentação
- Compartilhar seus aprendizados

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 🙏 Agradecimentos

- **Agno Team** - Pelo framework incrível
- **Anthropic** - Pelo Claude
- **Comunidade** - Por todo o suporte

---

Feito com ❤️ usando [Agno](https://docs.agno.com/)


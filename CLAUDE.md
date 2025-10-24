# CLAUDE.md - Projeto Agente Básico com Agno

## A Regra de Ouro
Quando não tiver certeza sobre detalhes de implementação, SEMPRE pergunte ao desenvolvedor.

## Contexto do Projeto
Este é um projeto de aprendizado para criar agentes básicos usando o framework Agno.
O objetivo é construir agentes simples, funcionais e bem documentados.

## Arquitetura

### Por que Agno?
- Framework mais rápido para multi-agentes (529× mais rápido que LangGraph)
- Runtime FastAPI pronto para produção
- Suporte nativo a MCP (Model Context Protocol)
- Private by design - roda totalmente local
- Memória e conhecimento persistentes

### Stack Tecnológica
- **Framework**: Agno v2.x
- **Modelo**: Claude Sonnet 4 (Anthropic)
- **Database**: SQLite (para desenvolvimento)
- **Runtime**: AgentOS (FastAPI)
- **Python**: 3.10+

## Comandos Bash Comuns

```bash
# Ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar o agente
python agente_basico.py

# Rodar com reload automático
python agente_basico.py --reload

# Acessar UI do AgentOS
# Abra o browser em: http://localhost:7777
```

## Estilo de Código

### Formatação
- Use type hints em todas as funções
- Docstrings em português para este projeto
- Imports organizados: stdlib → terceiros → locais
- Linhas com máximo de 100 caracteres

### Padrões Python
```python
# BOM: Type hints e docstrings claros
def criar_agente(nome: str, modelo: str) -> Agent:
    """Cria um agente básico do Agno.
    
    Args:
        nome: Nome identificador do agente
        modelo: ID do modelo a ser usado
        
    Returns:
        Instância configurada do Agent
    """
    pass

# RUIM: Sem tipos nem documentação
def criar_agente(nome, modelo):
    pass
```

### Anchor Comments
Use comentários especiais para guiar o desenvolvimento:

- `# AIDEV-NOTE:` - Informação importante sobre o código
- `# AIDEV-TODO:` - Tarefa pendente
- `# AIDEV-QUESTION:` - Dúvida que precisa ser esclarecida
- `# AIDEV-ANSWER:` - Resposta para uma AIDEV-QUESTION anterior

Exemplo:
```python
# AIDEV-NOTE: Este agente usa SQLite em dev, mas deve usar PostgreSQL em prod
db = SqliteDb(db_file="agente.db")

# AIDEV-TODO: Adicionar suporte para ferramentas customizadas (ticket: AG-123)
tools = [MCPTools(...)]

# AIDEV-QUESTION: Por que não usar memória em memória aqui?
# AIDEV-ANSWER: Precisamos persistir o histórico entre reinicializações
```

## Estrutura do Projeto

```
agno_agent_reslmidor/
├── CLAUDE.md                 # Este arquivo
├── README.md                 # Documentação do projeto
├── requirements.txt          # Dependências Python
├── .env.example             # Template de variáveis de ambiente
├── .gitignore               # Arquivos a ignorar no git
├── agente_basico.py         # Agente principal
├── agente.db                # Database SQLite (gerado automaticamente)
└── tests/                   # Testes (humanos escrevem!)
    └── test_agente.py
```

## Padrões do Agno

### Criação de Agent
```python
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.db.sqlite import SqliteDb

agent = Agent(
    name="Nome Descritivo",           # Nome do agente
    model=Claude(id="claude-sonnet-4-5"),  # Modelo LLM
    db=SqliteDb(db_file="db.db"),    # Database para persistência
    tools=[...],                      # Ferramentas disponíveis
    add_history_to_context=True,     # Adiciona histórico ao contexto
    markdown=True,                    # Formata saída em markdown
)
```

### Criação de AgentOS
```python
from agno.os import AgentOS

agent_os = AgentOS(agents=[agent1, agent2])  # Pode ter múltiplos agentes
app = agent_os.get_app()  # Retorna app FastAPI
```

### Servindo o AgentOS
```python
if __name__ == "__main__":
    agent_os.serve(
        app="nome_arquivo:app",  # Formato: "arquivo:variavel_app"
        reload=True,              # Hot reload em desenvolvimento
        host="0.0.0.0",          # Aceita conexões externas
        port=7777,               # Porta padrão do AgentOS
    )
```

## Variáveis de Ambiente

Sempre use variáveis de ambiente para segredos:

```python
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega .env

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
```

**NUNCA** commite chaves API ou segredos no código!

## Workflow de Desenvolvimento

### 1. Explorar e Planejar
- Leia a documentação do Agno
- Entenda os requisitos
- Faça um plano antes de codificar

### 2. Implementar
- Crie o agente seguindo os padrões
- Adicione comentários anchor onde apropriado
- Use type hints

### 3. Testar
- **HUMANOS ESCREVEM OS TESTES**
- Testes são especificações executáveis
- Nunca modifique testes para fazê-los passar

### 4. Documentar
- Atualize README.md se necessário
- Adicione docstrings
- Mantenha CLAUDE.md atualizado

## O Que a IA NUNCA Deve Fazer

❌ **NUNCA modifique arquivos de teste** - Testes codificam intenção humana
❌ **NUNCA commite segredos** - Use variáveis de ambiente
❌ **NUNCA assuma lógica de negócio** - Sempre pergunte
❌ **NUNCA remova AIDEV- comments** - Estão lá por um motivo

## Recursos Úteis

- **Docs Agno**: https://docs.agno.com/
- **Cookbook Agno**: https://github.com/agno-agi/agno/tree/main/cookbook
- **MCP Docs**: https://modelcontextprotocol.io/
- **Anthropic API**: https://docs.anthropic.com/

## Princípios

1. **Simplicidade primeiro** - Comece simples, adicione complexidade quando necessário
2. **Performance importa** - Agno é rápido, mantenha assim
3. **Privacidade é fundamental** - Tudo roda local
4. **Documentação é código** - Documente enquanto desenvolve
5. **Testes são sagrados** - Proteja-os zelosamente

---

Lembre-se: Otimizamos para manutenibilidade acima de inteligência. Quando em dúvida, escolha a solução mais simples e chata.


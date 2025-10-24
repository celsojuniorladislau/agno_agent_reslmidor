"""
Agente Básico com Agno

Este é um exemplo de agente básico usando o framework Agno.
O agente usa Claude Sonnet 4, tem memória persistente e pode ser
acessado via interface web através do AgentOS.

Uso:
    python agente_basico.py

Acesse em:
    http://localhost:7777

Documentação oficial:
    https://docs.agno.com/
"""

import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.anthropic import Claude
from agno.os import AgentOS
from agno.tools.mcp import MCPTools

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# AIDEV-NOTE: Verificar se a chave API está configurada
# É crítico validar antes de inicializar o agente
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise ValueError(
        "ANTHROPIC_API_KEY não encontrada! "
        "Copie .env.example para .env e adicione sua chave API."
    )

# AIDEV-NOTE: Setup do database no nível do módulo
# SQLite é ideal para desenvolvimento, PostgreSQL recomendado para produção
db = SqliteDb(db_file="agente.db")

# AIDEV-NOTE: Criação do agente no nível do módulo seguindo padrões oficiais
# Referência: https://docs.agno.com/introduction/quickstart
agno_agent = Agent(
    # AIDEV-NOTE: ID único para identificar o agente no sistema
    id="agente-basico",
    
    # Nome e descrição do agente
    name="Agente Básico",
    description="Um agente básico para demonstração do framework Agno",
    
    # AIDEV-NOTE: Claude Sonnet 4.5 é o modelo mais recente e performático
    model=Claude(id="claude-sonnet-4-5"),
    
    # Database para persistir conversas e memória
    db=db,
    
    # AIDEV-NOTE: MCPTools permite que o agente acesse a documentação do Agno
    # Isso torna o agente self-aware sobre suas próprias capacidades
    tools=[
        MCPTools(
            transport="streamable-http",
            url="https://docs.agno.com/mcp"
        )
    ],
    
    # AIDEV-NOTE: Configurações de histórico e contexto
    # Adiciona histórico de conversas ao contexto para continuidade
    add_history_to_context=True,
    
    # AIDEV-NOTE: num_history_runs controla quantas interações anteriores
    # são incluídas no contexto (padrão da documentação: 3)
    num_history_runs=3,
    
    # AIDEV-NOTE: Adiciona timestamp ao contexto para referências temporais
    add_datetime_to_context=True,
    
    # AIDEV-NOTE: Habilita sumarização automática de sessões longas
    # Isso mantém o contexto gerenciável mesmo em conversas extensas
    enable_session_summaries=True,
    
    # Formata saídas em Markdown para melhor legibilidade
    markdown=True,
)

# AIDEV-NOTE: Setup do AgentOS no nível do módulo (padrão oficial)
# Isso permite que o FastAPI encontre a app corretamente
agent_os = AgentOS(
    id="agentos-basico",
    description="AgentOS básico com Claude e MCP",
    agents=[agno_agent],
)

# AIDEV-NOTE: Obtém a aplicação FastAPI no nível do módulo
# Isso é necessário para o uvicorn encontrar a app
app = agent_os.get_app()


def main():
    """
    Função principal que serve o AgentOS.
    
    Esta função imprime informações úteis e inicia o servidor.
    O AgentOS já foi configurado no nível do módulo seguindo
    os padrões oficiais da documentação.
    """
    print(">>> Inicializando Agente Basico com Agno...")
    print(f"[OK] Agente '{agno_agent.name}' (ID: {agno_agent.id}) criado com sucesso!")
    print(f"Modelo: {agno_agent.model.id}")
    print(f"Database: {db.db_file}")
    print(f"Historico: ultimas {agno_agent.num_history_runs} interacoes")
    
    print("\n" + "="*60)
    print(">>> AgentOS iniciado com sucesso!")
    print("="*60)
    print("\n>>> Acesse a interface web em:")
    print("    http://localhost:7777")
    print("\n>>> Documentacao da API:")
    print("    http://localhost:7777/docs")
    print("\n>>> Dicas:")
    print("  - A interface permite conversar com o agente")
    print("  - O historico e salvo automaticamente no SQLite")
    print("  - Sessoes longas sao sumarizadas automaticamente")
    print("  - Use Ctrl+C para parar o servidor")
    print("\n" + "="*60 + "\n")
    
    # AIDEV-NOTE: serve() inicia o servidor FastAPI
    # reload=True permite hot-reload durante desenvolvimento
    # IMPORTANTE: não use reload=True em produção
    agent_os.serve(
        app="agente_basico:app",
        reload=True,
        host="0.0.0.0",  # Aceita conexões de qualquer IP
        port=7777,       # Porta padrão do AgentOS
    )


if __name__ == "__main__":
    main()


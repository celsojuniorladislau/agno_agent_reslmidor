"""
Testes para o Agente Básico

IMPORTANTE: Estes testes são escritos por HUMANOS e codificam a intenção
e especificações do sistema. IA NUNCA deve modificar estes arquivos.

Para rodar os testes:
    python -m pytest tests/
    
Para rodar com verbose:
    python -m pytest tests/ -v
"""

import pytest
import os
from unittest.mock import patch, MagicMock


def test_anthropic_api_key_validation():
    """
    Testa se o sistema valida corretamente a presença da chave API.
    
    Especificação:
    - Se ANTHROPIC_API_KEY não estiver configurada, deve lançar ValueError
    - A mensagem de erro deve ser clara e indicar o que fazer
    """
    # Simula ausência da chave API
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError) as exc_info:
            # Importar vai tentar carregar a chave e deve falhar
            import importlib
            import sys
            
            # Remove módulo se já foi importado
            if 'agente_basico' in sys.modules:
                del sys.modules['agente_basico']
            
            import agente_basico
        
        # Verifica se a mensagem é útil
        assert "ANTHROPIC_API_KEY" in str(exc_info.value)


def test_agente_tem_id_unico():
    """
    Testa se o agente tem um ID único definido.
    
    Especificação:
    - O agente deve ter um ID único "agente-basico"
    - Este ID é usado para identificar o agente no sistema
    """
    with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'sk-ant-test-key'}):
        from agente_basico import agno_agent
        
        assert agno_agent.id == "agente-basico"


def test_agente_tem_nome_correto():
    """
    Testa se o agente é criado com o nome esperado.
    
    Especificação:
    - O agente deve ter o nome "Agente Básico"
    - Este nome é usado na interface e logs
    """
    with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'sk-ant-test-key'}):
        from agente_basico import agno_agent
        
        assert agno_agent.name == "Agente Básico"


def test_agente_tem_descricao():
    """
    Testa se o agente tem uma descrição configurada.
    
    Especificação:
    - A descrição ajuda outros sistemas a entender o propósito do agente
    """
    with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'sk-ant-test-key'}):
        from agente_basico import agno_agent
        
        assert hasattr(agno_agent, 'description')
        assert agno_agent.description is not None
        assert len(agno_agent.description) > 0


def test_agente_usa_claude_sonnet_4():
    """
    Testa se o agente está configurado para usar Claude Sonnet 4.5
    
    Especificação:
    - Deve usar especificamente claude-sonnet-4-5
    - Este é o modelo mais recente e performático da Anthropic
    """
    with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'sk-ant-test-key'}):
        from agente_basico import agno_agent
        
        assert agno_agent.model.id == "claude-sonnet-4-5"


def test_agente_tem_database_configurado():
    """
    Testa se o agente tem database para persistência.
    
    Especificação:
    - Deve ter um database configurado (SQLite em dev)
    - Isso permite persistir conversas entre sessões
    """
    with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'sk-ant-test-key'}):
        from agente_basico import agno_agent
        
        assert agno_agent.db is not None
        assert hasattr(agno_agent.db, 'db_file')


def test_agente_tem_historico_habilitado():
    """
    Testa se o agente adiciona histórico ao contexto.
    
    Especificação:
    - add_history_to_context deve estar True
    - Isso permite que o agente "lembre" de conversas anteriores
    """
    with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'sk-ant-test-key'}):
        from agente_basico import agno_agent
        
        assert agno_agent.add_history_to_context is True


def test_agente_tem_num_history_runs_configurado():
    """
    Testa se o agente tem controle de quantas interações são mantidas.
    
    Especificação:
    - num_history_runs deve estar configurado (padrão: 3)
    - Controla quantas conversas anteriores são incluídas no contexto
    """
    with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'sk-ant-test-key'}):
        from agente_basico import agno_agent
        
        assert agno_agent.num_history_runs == 3


def test_agente_tem_datetime_habilitado():
    """
    Testa se o agente adiciona timestamp ao contexto.
    
    Especificação:
    - add_datetime_to_context deve estar True
    - Permite referências temporais nas conversas
    """
    with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'sk-ant-test-key'}):
        from agente_basico import agno_agent
        
        assert agno_agent.add_datetime_to_context is True


def test_agente_tem_session_summaries_habilitado():
    """
    Testa se o agente tem sumarização de sessões habilitada.
    
    Especificação:
    - enable_session_summaries deve estar True
    - Mantém contexto gerenciável em conversas longas
    """
    with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'sk-ant-test-key'}):
        from agente_basico import agno_agent
        
        assert agno_agent.enable_session_summaries is True


def test_agente_tem_markdown_habilitado():
    """
    Testa se o agente formata saídas em Markdown.
    
    Especificação:
    - markdown deve estar True
    - Melhora a legibilidade das respostas
    """
    with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'sk-ant-test-key'}):
        from agente_basico import agno_agent
        
        assert agno_agent.markdown is True


def test_agente_tem_tools_mcp():
    """
    Testa se o agente tem ferramentas MCP configuradas.
    
    Especificação:
    - Deve ter pelo menos uma ferramenta (MCPTools)
    - MCPTools dá acesso à documentação do Agno
    """
    with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'sk-ant-test-key'}):
        from agente_basico import agno_agent
        
        assert agno_agent.tools is not None
        assert len(agno_agent.tools) > 0


def test_agentos_tem_id_configurado():
    """
    Testa se o AgentOS tem um ID único configurado.
    
    Especificação:
    - AgentOS deve ter ID "agentos-basico"
    - Útil para ambientes com múltiplos AgentOS
    """
    with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'sk-ant-test-key'}):
        from agente_basico import agent_os
        
        assert agent_os.id == "agentos-basico"


# AIDEV-NOTE: Adicione mais testes conforme o agente evolui
# Cada teste deve codificar uma especificação clara do comportamento esperado


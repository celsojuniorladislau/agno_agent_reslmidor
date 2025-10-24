"""Script de teste para verificar se tudo esta funcionando"""
print("=" * 60)
print(">>> Testando imports...")
print("=" * 60)

try:
    from agente_basico import agno_agent, agent_os, app
    print("[OK] Imports funcionaram!")
    print(f"\nAgent Name: {agno_agent.name}")
    print(f"Agent ID: {agno_agent.id}")
    print(f"Model: {agno_agent.model.id}")
    print(f"AgentOS ID: {agent_os.id}")
    print("\n" + "=" * 60)
    print("[SUCESSO] TUDO FUNCIONANDO!")
    print("=" * 60)
    print("\nPara rodar o servidor, execute:")
    print("   python agente_basico.py")
except Exception as e:
    print(f"\n[ERRO]: {e}")
    import traceback
    traceback.print_exc()


# 🚀 Início Rápido - 5 Minutos

## Passo 1: Instalar Dependências

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate

# Instalar
pip install -r requirements.txt
```

## Passo 2: Configurar Chave API

1. Vá em: https://console.anthropic.com/
2. Crie uma chave API
3. Copie o arquivo:

```bash
cp .env.example .env
```

4. Edite `.env` e adicione sua chave:

```
ANTHROPIC_API_KEY=sk-ant-sua-chave-aqui
```

## Passo 3: Rodar!

```bash
python agente_basico.py
```

## Passo 4: Acessar

Abra seu navegador em: **http://localhost:7777**

🎉 Pronto! Comece a conversar com seu agente.

---

## Testando

```bash
# Rodar testes
python -m pytest tests/

# Com verbose
python -m pytest tests/ -v
```

## Problemas?

Veja o [README.md](README.md) completo ou a seção Troubleshooting.


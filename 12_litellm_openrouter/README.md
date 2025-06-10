# 🚀 OpenRouter & LiteLLM Learning Project

A comprehensive learning project to understand how **OpenRouter** and **LiteLLM** work for accessing multiple AI models through unified interfaces.

## 📚 What You'll Learn

1. **OpenRouter**: How to access 100+ AI models through a single API endpoint
2. **LiteLLM**: How to use a unified interface for multiple AI providers
3. **API Key Management**: Secure ways to handle API credentials

## 🛠️ Setup Instructions

### 1. Install Dependencies

```bash
# Install using uv (recommended)
uv init litellm_openrouter
cd litellm_openrouter

# create a virtual environment
uv venv

# activate the virtual environment
.venv\Scripts\activate

# install dependencies
uv add litellm openai python-dotenv


uv sync
```

### 2. Configure API Keys

```bash
# Copy the example environment file
cp env.example .env

# Edit .env with your actual API keys
# You only need keys for the services you want to test
```

Get your API keys:
- **OpenRouter**: [https://openrouter.ai/keys](https://openrouter.ai/keys) (has free models!)
- **OpenAI**: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Anthropic**: [https://console.anthropic.com/](https://console.anthropic.com/)

### 3. Run the Program

```bash

# test individual components
uv run try_openrouter.py  # OpenRouter only
uv run try_litellm.py     # LiteLLM only
```

## 📖 Additional Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [LiteLLM Documentation](https://docs.litellm.ai/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Python AsyncIO Tutorial](https://docs.python.org/3/library/asyncio.html)


## ⚠️ Security Note

**Never commit API keys to version control!**
- Use `.env` files for secrets
- Add `.env` to your `.gitignore`
- Use environment variables in production

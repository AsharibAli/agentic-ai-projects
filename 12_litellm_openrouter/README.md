# 🚀 OpenRouter & LiteLLM Learning Project

A comprehensive learning project to understand how **OpenRouter** and **LiteLLM** work for accessing multiple AI models through unified interfaces.

## 📚 What You'll Learn

1. **OpenRouter**: How to access 100+ AI models through a single API endpoint
2. **LiteLLM**: How to use a unified interface for multiple AI providers
3. **API Key Management**: Secure ways to handle API credentials
4. **Error Handling**: How to build robust AI applications
5. **Async Programming**: Making efficient API calls
6. **Streaming**: Real-time AI responses

## 🛠️ Setup Instructions

### 1. Install Dependencies

```bash
# Install using uv (recommended)
uv sync

# Or using pip
pip install -e .
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
# Run the complete learning demo
python main.py

# Or test individual components
python openrouter.py  # OpenRouter only
python litellm.py     # LiteLLM only
```

## 📁 Project Structure

```
litellm-openrouter/
├── main.py          # Main program orchestrating all demos
├── openrouter.py    # OpenRouter API demonstrations
├── litellm.py       # LiteLLM demonstrations  
├── env.example      # Environment variables template
├── pyproject.toml   # Python dependencies
└── README.md        # This file
```

## 🎯 What Each File Does

### `main.py`
The entry point that:
- Shows you what the project will demonstrate
- Checks for API keys
- Runs both OpenRouter and LiteLLM demos
- Provides helpful error messages

### `openrouter.py`
Demonstrates OpenRouter usage:
- **Method 1**: Using OpenAI SDK with OpenRouter (recommended)
- **Method 2**: Direct HTTP API calls (educational)
- **Method 3**: Listing available models
- Shows how OpenRouter provides access to many AI models through one endpoint

### `litellm.py`
Demonstrates LiteLLM capabilities:
- **Multiple Providers**: Same code works with OpenAI, Anthropic, Google, etc.
- **Streaming**: Real-time responses
- **Async Calls**: Efficient API usage
- **Error Handling**: Robust error management
- **Embeddings**: Text-to-vector conversion

## 🆓 Free Models to Try

You can test without any API keys using these free models:

- **OpenRouter Free Models**:
  - `meta-llama/llama-3.2-3b-instruct:free`
  - `microsoft/phi-3-mini-128k-instruct:free`

## 💡 Key Learning Concepts

### OpenRouter Benefits
- **Single API**: Access 100+ models through one endpoint
- **Fallback Logic**: Automatic failover between models
- **Cost Optimization**: Route to cheapest available model
- **Free Models**: Test without spending money

### LiteLLM Benefits
- **Provider Abstraction**: Same code works across all providers
- **Consistent Interface**: OpenAI-style API for everything
- **Error Normalization**: Consistent error handling
- **Feature Parity**: Streaming, async, embeddings work everywhere

## 🔧 Common Issues & Solutions

### "No API key found"
- Copy `env.example` to `.env`
- Add your actual API keys
- You only need keys for services you want to test

### "Invalid API key"
- Check your API key is correct
- Ensure it has the right permissions
- Try the free models first

### "Rate limit exceeded"
- You're making requests too quickly
- Wait a moment and try again
- Consider using free models for testing

### "Model not found"
- Check the model name is correct
- Some models require specific API keys
- Try a different model

## 🚀 Next Steps

After running this project, try:

1. **Build a simple chatbot** using what you learned
2. **Compare different models** for your use case
3. **Implement fallback logic** for production apps
4. **Add streaming** for better user experience
5. **Use embeddings** for semantic search

## 📖 Additional Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [LiteLLM Documentation](https://docs.litellm.ai/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Python AsyncIO Tutorial](https://docs.python.org/3/library/asyncio.html)

## 🤝 Contributing

This is a learning project! Feel free to:
- Add more model examples
- Improve error handling
- Add new features
- Share your learning insights

## ⚠️ Security Note

**Never commit API keys to version control!**
- Use `.env` files for secrets
- Add `.env` to your `.gitignore`
- Use environment variables in production

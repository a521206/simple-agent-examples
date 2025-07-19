# Routing Examples

Examples of intelligent message routing using different frameworks.

## LangGraph Routing

A customer service routing system that automatically directs inquiries to specialized agents based on message content.

### Features

- **Intelligent Routing**: Routes messages to appropriate agents based on keywords
- **Specialized Agents**: 
  - Support Agent: General customer service
  - Order Agent: Order management, tracking, returns
  - Product Agent: Product information and recommendations
- **State Management**: Maintains conversation context through LangGraph state
- **Extensible**: Easy to add new agents and routing rules

### Usage

```bash
# Install dependencies
pip install langgraph langchain-openai python-dotenv

# Set up environment
cp config/env.example .env
# Add your OPENAI_API_KEY to .env

# Run the example
python examples/routing/langgraph_routing.py
```

### How It Works

1. **Router Function**: Analyzes incoming messages for keywords
2. **Agent Selection**: Routes to appropriate specialized agent
3. **Response Generation**: Each agent uses LLM with specific system prompts
4. **State Management**: Maintains conversation history and context

### Example Queries

- "What's my order status?" → Order Agent
- "Tell me about product features" → Product Agent  
- "I need help with my account" → Support Agent
- "Can I return this item?" → Order Agent
- "Compare these products" → Product Agent

### Customization

To add new agents:

1. Define new agent function
2. Add routing keywords to router function
3. Update workflow graph with new node and edges 
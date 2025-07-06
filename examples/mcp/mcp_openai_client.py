# WARNING: OpenAI MCP integration is currently facing issues and may not work properly.
# The code below is kept for reference but may not function as expected.
# This issue may be resolved in future versions of the OpenAI library.

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    tools=[{
        "type": "mcp",
        "server_label": "MathTools",
        "server_url": "https://49e6-49-205-241-155.ngrok-free.app/mcp",
        "require_approval": "never"
    }],
    input="Convert 100 USD to EUR?"
)

print(response.output_text)

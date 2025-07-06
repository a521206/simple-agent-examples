from fastmcp import FastMCP
import asyncio
from pydantic import BaseModel, Field

# Create MCP app
mcp = FastMCP(name="Currency Tools")

# TODO: Replace with real API call to currency exchange service
CURRENCY_RATES = {
    "USD": {"EUR": 0.85, "GBP": 0.75, "JPY": 110.0},
    "EUR": {"USD": 1.2, "GBP": 0.9, "JPY": 130.0},
    "GBP": {"USD": 1.5, "EUR": 1.25, "JPY": 150.0},
    "JPY": {"USD": 0.01, "EUR": 0.01, "GBP": 0.01}
} 

class CurrencyConversionInput(BaseModel):
    amount: float = Field(..., description="Amount to convert")
    from_currency: str = Field(..., description="Source currency code (e.g., 'USD', 'EUR')")
    to_currency: str = Field(..., description="Target currency code (e.g., 'EUR', 'GBP')")

@mcp.tool()
async def convert_currency(request: CurrencyConversionInput) -> str:
    """Convert between different currencies using current exchange rates."""
    amount = request.amount
    from_curr = request.from_currency.upper()
    to_curr = request.to_currency.upper()
    
    if from_curr not in CURRENCY_RATES:
        return f"Unsupported currency: {from_curr}"
    
    if to_curr not in CURRENCY_RATES[from_curr]:
        return f"Conversion not available: {from_curr} to {to_curr}"
    
    rate = CURRENCY_RATES[from_curr][to_curr]
    converted_amount = amount * rate
    
    return f"{amount} {from_curr} = {converted_amount:.2f} {to_curr}"

@mcp.tool()
async def get_supported_currencies() -> str:
    """List all supported currencies and their conversion pairs."""
    result = "Supported currencies:\n"
    for base_currency in CURRENCY_RATES:
        result += f"{base_currency}: {', '.join(CURRENCY_RATES[base_currency].keys())}\n"
    return result

# Optional: Print available tools
async def show_tools():
    tools = await mcp.get_tools()
    print("🧰 Available Tools:")
    for name in tools:
        print(f" - {name}")

# Run the server
if __name__ == "__main__":
    print("🚀 Starting FastMCP Currency Server on port 8000...")
    asyncio.run(show_tools())
    mcp.run(transport="http", port=8000)

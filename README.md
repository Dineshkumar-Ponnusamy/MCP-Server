# Weather Agent MCP Server

A sample MCP server that provides weather information for a specified city using the OpenWeatherMap API.

## Description

This project implements a simple Model Context Protocol (MCP) server called "Weather Bot". It exposes a single tool that fetches current weather data for a given city, including temperature in Celsius, humidity, and weather description. The server communicates via standard I/O (stdio) and can be integrated with MCP-compatible clients.

Tested on Apple M1 Air.

## Features

- Get current weather information for any city
- Returns formatted weather data including description, temperature (°C), and humidity
- Integrates with OpenWeatherMap API for up-to-the-minute weather data

## Installation

1. Clone or download this repository to your local machine.

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Get an API key from [OpenWeatherMap](https://openweathermap.org/api)

2. Create a `.env` file in the project root and add your API key:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```
   **Security Note:** Never commit your `.env` file to version control. Ensure it's included in your `.gitignore`.

## Usage

Run the MCP server using:

```
python weather_agent.py
```

The server starts and listens for MCP protocol messages via stdio. It can be integrated with MCP-compatible applications or clients.

## Integration with Claude Desktop

To test this MCP server with Claude Desktop, follow these steps:

1. Ensure Claude Desktop is installed on your machine.

2. Locate your `claude_desktop_config.json` file. On macOS, it's typically located at `~/Library/Application Support/Claude/claude_desktop_config.json`. You can also open the path by openging via UI, Claude > Settings > Developer > Edit Config.

3. Open the `claude_desktop_config.json` file and add the following configuration inside the JSON object (add to the "mcpServers" object if it exists, or create it):

```json
{
  "mcpServers": {
    "weather-agent": {
      "command": "python",
      "args": ["/path/to/your/mcp-server/weather_agent.py"]
    }
  }
}
```

Replace `/path/to/your/mcp-server/weather_agent.py` with the absolute path to your `weather_agent.py` file. For example, the path might be `/Users/yourusername/Desktop/mcp-server/weather_agent.py`.

4. Save the `claude_desktop_config.json` file.

5. Restart Claude Desktop to load the new configuration.

6. In Claude Desktop, you can now interact with the weather agent. For example, ask Claude: "What's the weather in Tokyo?" and it should use the MCP server to fetch and return the weather information.

**Note:** Ensure that your API key is configured in the `.env` file as described in the Configuration section, and that the Python environment is set up to run the script (e.g., the required packages are installed).

## API

### get_weather(city: str) -> str

Fetches current weather information for the specified city.

**Parameters:**

- `city`: String - The name of the city to get weather for

**Returns:**
A formatted string containing:

- City name
- Weather description
- Current temperature in Celsius
- Humidity percentage

**Example Response:**

```
The current weather in London is overcast clouds with a temperature of 15°C and humidity of 72%.
```

## Dependencies

- `requests`: For making HTTP requests to the weather API
- `python-dotenv`: For loading environment variables from .env file
- `fastmcp`: MCP server framework

## Error Handling

If the weather API returns an error or the city is not found, the tool will return an error message indicating the failure to fetch data.

## License

This is a sample project. Feel free to modify and use as needed.


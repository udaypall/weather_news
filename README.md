# 🌦️ AutoGen Weather News Agent

An AI-powered Weather News Agent built using **Microsoft AutoGen, OpenAI GPT-4o-mini, and DuckDuckGo Search**.

The agent accepts a city name from the user, searches for today's weather-related news using DuckDuckGo, and uses OpenAI to analyze the search results and generate a concise three-point weather report.

## 🔗 GitHub Repository

**Repository:** [https://github.com/udaypall/weather_news](https://github.com/udaypall/weather_news)

## 🚀 Features

- Accepts any city name as user input.
- Searches weather-related news using DuckDuckGo.
- Uses the free, keyless `ddgs` search package.
- Integrates OpenAI GPT-4o-mini through AutoGen.
- Uses a custom Python function as an AutoGen tool.
- AI filters irrelevant search results and summarizes useful information.
- Generates exactly three concise bullet points.
- Keeps API credentials in environment variables.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Microsoft AutoGen | AI agent framework |
| OpenAI GPT-4o-mini | Analysis and summarization |
| DuckDuckGo (`ddgs`) | Weather news search |
| python-dotenv | Environment variable management |

## 📁 Project Structure

```text
weather_news/
│
├── venv/
├── .env
├── .gitignore
├── requirements.txt
├── weather_news.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```cmd
git clone https://github.com/udaypall/weather_news.git
cd weather_news
```

### 2. Create a virtual environment

```cmd
python -m venv venv
```

### 3. Activate the virtual environment

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```cmd
pip install -U autogen-agentchat "autogen-ext[openai]" ddgs python-dotenv
```

### 5. Configure the OpenAI API key

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=your_openai_api_key
```

**Important:** Never upload your `.env` file or expose your API key on GitHub.

### 6. Run the application

```cmd
py weather_news.py
```

## 🔄 How It Works

1. **User Input:** The user enters a city name.
2. **DuckDuckGo Search:** A Python function searches for up to five weather-related news articles.
3. **AutoGen Agent:** The search function is registered as a tool using `tools=[search_weather_news]`.
4. **OpenAI Analysis:** GPT-4o-mini analyzes the search results, ignores irrelevant information and summarizes the weather updates.
5. **Final Response:** The agent generates exactly three concise bullet points.

## 💻 Sample Execution

```text
Which city? Chennai

Starting Weather News Agent...

---------- ToolCallRequestEvent (weather_news) ----------
search_weather_news(city='Chennai')

---------- ToolCallExecutionEvent (weather_news) ----------
[DuckDuckGo search results]

---------- TextMessage (weather_news) ----------

- 🌦️ Weather: Current weather conditions based on relevant reports.
- 🌧️ Forecast: Rainfall and important weather alerts.
- ⚠️ Advisory: Relevant weather precautions.

Weather News Agent execution completed.
```

*The output is illustrative. Actual results depend on DuckDuckGo search availability and the information retrieved.*

## 🧠 Key AutoGen Concepts Learned

- Creating an AI agent using `AssistantAgent`.
- Integrating OpenAI GPT-4o-mini with AutoGen.
- Creating custom Python tools using function definitions.
- Using type hints and docstrings to describe tools.
- Registering tools with `tools=[search_weather_news]`.
- Understanding `reflect_on_tool_use=True`.
- Streaming agent execution using `Console`.
- Managing asynchronous execution with `asyncio`.
- Securely managing API keys using environment variables.

## 🔑 Important Configuration

The project uses:

```python
reflect_on_tool_use=True
```

This enables the agent to analyze the tool execution results and generate a meaningful final response instead of simply returning raw search results.

## ⚠️ Limitations

- DuckDuckGo search results may contain unrelated articles.
- Weather news availability varies by city.
- OpenAI summarizes retrieved information; it does not independently verify live weather conditions.
- The agent should report unavailable information rather than invent forecasts.

## 🎯 Assignment Objective

To understand how an AI agent moves beyond simple conversations by using external Python functions as tools, retrieving information from the web, and applying an LLM to analyze and generate useful responses.

---

**Built with Python, AutoGen, DuckDuckGo and OpenAI GPT-4o-mini.**
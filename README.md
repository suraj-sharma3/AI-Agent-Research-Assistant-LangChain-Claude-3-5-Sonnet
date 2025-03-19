# AI-Agent-Research-Assistant-LangChain

### Generate Claude API key from https://console.anthropic.com/settings/keys
### Generate ChatGPT API key from https://platform.openai.com/api-keys

# AI-Powered Research Assistant  

## Overview  
The **AI Agent Research Assistant** is an **intelligent tool** designed to automate the process of **gathering, summarizing, and storing research data**. It integrates **Anthropic's Claude-3.5-Sonnet AI model** with external tools to **search the web, fetch Wikipedia summaries, and save structured research findings** to a file. This project ensures well-organized research outputs, making it easy for users to retrieve valuable insights, sources, and methodologies.  

## Features  
✅ **AI-Driven Research** – Uses **Claude-3.5-Sonnet** for advanced research-based responses.  
✅ **Web Search Integration** – Retrieves **relevant online information** using **DuckDuckGo Search**.  
✅ **Wikipedia Lookup** – Fetches **concise Wikipedia summaries** for research topics.  
✅ **Structured Output** – Uses **Pydantic models** to organize research into **topics, summaries, sources, and tools used**.  
✅ **Automated Research Storage** – Saves research findings in a structured text file for future reference.  
✅ **Tool-Calling Agent** – The AI dynamically selects and executes tools for enhanced research efficiency.  

## How It Works  
1. The user inputs a research query.  
2. The AI agent processes the query using a **predefined prompt template**.  
3. The assistant calls relevant tools (**search, Wikipedia lookup, or save**) as needed.  
4. The **response is structured and parsed** into a formatted research output.  
5. The final research findings are **displayed and optionally saved** to a file.  

## Technologies Used  
- **Python** – Core programming language  
- **LangChain** – AI model orchestration and tool-calling capabilities  
- **Anthropic Claude-3.5-Sonnet** – AI model for generating research insights  
- **DuckDuckGo Search API** – For retrieving online information  
- **Wikipedia API** – For fetching relevant summaries  
- **Pydantic** – For structured data parsing and validation  
- **dotenv** – For secure environment variable management  

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/suraj-sharma3/AI-Agent-Research-Assistant-LangChain-Claude-3-5-Sonnet.git
   cd AI-Agent-Research-Assistant-LangChain-Claude-3-5-Sonnet
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:  
   - Create a `.env` file and add your **Anthropic API key**:  
     ```
     ANTHROPIC_KEY=your_api_key_here
     ```
4. Run the assistant:  
   ```bash
   python main.py
   ```

## Usage  
- **Simply enter a research topic** when prompted.  
- The assistant will **fetch information, summarize findings, and present a structured response**.  
- If required, the results can be **saved to a file** for later use.  

## Example Output  
```json
{
  "topic": "Artificial Intelligence in Healthcare",
  "summary": "AI is revolutionizing healthcare by enabling faster diagnostics, personalized treatment plans, and automation of administrative tasks.",
  "sources": [
    "https://www.healthcare-ai.com",
    "https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare"
  ],
  "tools_used": ["DuckDuckGo Search", "Wikipedia API"]
}
```

## Future Improvements  
🔹 **Expand to additional AI models** (GPT, Gemini, etc.)  
🔹 **Enhance search capabilities** with more APIs  
🔹 **Improve data visualization** for research insights  

## 📌 Repository Link  
🔗 **[GitHub Repository](https://github.com/suraj-sharma3/AI-Agent-Research-Assistant-LangChain-Claude-3-5-Sonnet.git)**  


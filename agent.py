from dotenv import load_dotenv  # Load environment variables from a .env file
from pydantic import BaseModel  # Define structured data models with validation
from langchain_openai import ChatOpenAI  # Interface for OpenAI's chat models
from langchain_anthropic import ChatAnthropic  # Interface for Anthropic's chat models
from langchain_core.prompts import ChatPromptTemplate  # Create and manage prompt templates
from langchain_core.output_parsers import PydanticOutputParser  # Parse model outputs into Pydantic objects
from langchain.agents import create_tool_calling_agent, AgentExecutor  # Create and execute AI agents with tool-calling capabilities
from utils import search_tool, wiki_tool, save_tool
import os

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str = ""         # The main topic of the research
    summary: str = ""       # A short summary of the research findings
    sources: list[str] = [] # A list of sources used for the research
    tools_used: list[str] = [] # A list of tools or methods used in the research

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", api_key=os.getenv("ANTHROPIC_KEY"))  
# Creates an AI chat model instance using Anthropic's Claude model  
# The API key is securely loaded from environment variables  

parser = PydanticOutputParser(pydantic_object=ResearchResponse)  
# Sets up a parser to convert the AI model's response into a structured ResearchResponse object  
# Ensures the output follows the defined data model (with topic, summary, sources, and tools used)  

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),  # System message defining the AI's role and response format
        ("placeholder", "{chat_history}"),  # Placeholder for past conversation history
        ("human", "{query}"),  # Placeholder for the user's query
        ("placeholder", "{agent_scratchpad}"),  # Placeholder for the agent's intermediate reasoning steps
    ]
).partial(format_instructions=parser.get_format_instructions())  
# Provides format instructions for structuring the AI's response based on the Pydantic parser

tools = [search_tool, wiki_tool, save_tool]  
# List of tools the AI agent can use, such as a search tool, Wikipedia lookup tool, and a save tool  

agent = create_tool_calling_agent(
    llm=llm,  # The AI model (Claude) that will process user queries
    prompt=prompt,  # The structured prompt defining how the AI should respond
    tools=tools  # The tools available for the agent to use during research
)  
# Creates an AI agent that can call external tools to assist in answering queries  

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)  
# Creates an executor that runs the AI agent with the specified tools  
# The `verbose=True` flag enables detailed logging of the agent's actions, keep verbose true if you want to see the thinking or reasoning of the model for generating the response

query = input("What can I help you research? ")  
# Prompts the user to enter a research query  

raw_response = agent_executor.invoke({"query": query})  
# Executes the agent with the user's query and retrieves the AI's response  

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])  
    # Parses the AI's raw response into a structured ResearchResponse object  
    print(structured_response)  # Prints the formatted response  
except Exception as e:
    print("Error encountered while parsing the raw response:", e, 
          "Raw response from the LLM:", raw_response)  
    # Handles any errors that occur during parsing and prints the raw response for debugging  




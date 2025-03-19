from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun  # Import tools for searching Wikipedia and DuckDuckGo  
from langchain_community.utilities import WikipediaAPIWrapper  # Utility wrapper for interacting with the Wikipedia API  
from langchain.tools import Tool  # General class for defining custom tools that the AI agent can use  
from datetime import datetime  # Standard Python module for working with date and time  

def save_to_txt(data: str, filename: str = "research_data.txt"):
    """
    Saves the given research data to a text file with a timestamp.

    Parameters:
    - data (str): The research data to be saved.
    - filename (str, optional): The name of the file where data will be appended. Default is 'research_data.txt'.

    Returns:
    - str: Confirmation message indicating successful save.
    """
    # Get the current timestamp in a readable format
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format the data with a header and timestamp
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    # Open the file in append mode and write the formatted data
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Research data successfully saved to {filename}"

# Define a tool that uses the save_to_txt function to store research data
save_tool = Tool(
    name="save_data_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

# Initialize a DuckDuckGo search utility
search = DuckDuckGoSearchRun()

# Define a tool for performing internet searches using DuckDuckGo
search_tool = Tool(
    name="search",
    func=search.run,
    description="Searches the internet for information",
)

# Initialize a Wikipedia API wrapper with a limit on results and content length
wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=300)

# Define a tool for retrieving summarized Wikipedia content
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)
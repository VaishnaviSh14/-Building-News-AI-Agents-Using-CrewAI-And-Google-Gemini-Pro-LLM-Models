from crewai import Agent
from tools import tool

from dotenv import load_dotenv
load_dotenv()
import os
from crewai.llm import LLM

# Use CrewAI's LLM class instead
llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

#Create an agent who is senior researcher with memory and verbose mode
news_researcher=Agent(
    role="Senior researcher",
    goal = "Conduct in-depth research on a given {topic} and provide comprehensive insights.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned researcher with expertise in gathering and analyzing information from various sources. "
        "Your goal is to provide detailed and accurate insights on complex topics."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Creating a writer agent who will be responsible for writing news blog posts
news_writer=Agent(
    role="Writer",
    goal="Write engaging and informative news blog posts based on {topic}.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a skilled writer with a knack for transforming complex information into engaging and accessible content. "
        "Your goal is to create compelling news blog posts that captivate readers."
    ),
    llm=llm,
    tools=[tool],
    allow_delegation=False
)
from dotenv import load_dotenv
load_dotenv()
from crewai_tools import (
    SerperDevTool,
)

import os
os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")


#initialize the Serper Dev Tool
tool = SerperDevTool()

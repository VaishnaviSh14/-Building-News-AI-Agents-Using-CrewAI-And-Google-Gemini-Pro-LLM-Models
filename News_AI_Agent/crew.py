from crewai import Crew, Process
from tasks import researcher_task, writer_task
from agents import news_researcher, news_writer

crew=Crew(
    agents=[news_researcher, news_writer],
    tasks=[researcher_task, writer_task],
    process=Process.sequential
) 

# Starting the task execution process with enhanced feedback

result=crew.kickoff(inputs={"topic": "Artificial Intelligence in Healthcare"})
print(result)
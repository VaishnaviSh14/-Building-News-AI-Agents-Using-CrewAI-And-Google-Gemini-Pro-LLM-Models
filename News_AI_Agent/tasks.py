from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

researcher_task = Task(
    description=(
    "Identify the next big trend in {topic}. "
    "Focus on identifying pros and cons, key players, and potential future developments. "
    "Your final report should clearly articulate the key points and provide actionable insights. "
    "Include market opportunities, technological advancements, and societal impacts."
    ),
    expected_output="A comprehensive report detailing the next big trend in {topic}, including pros and cons, key players, and potential future developments.",
    tools=[tool],
    agent=news_researcher,
)

writer_task = Task(
    description=(
        "Write a detailed news blog post on the topic: {topic}. "
        "Focus on latest trends and how it is impacting the industry. "
        "This article should be engaging, informative, and well-structured."
    ),
    expected_output="A well-written news blog post on the topic: {topic}, covering latest trends and their impact on the industry.",
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file="news_blog_post.txt"
)

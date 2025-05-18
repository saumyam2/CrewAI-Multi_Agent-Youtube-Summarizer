from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

# llm = ChatOpenAI(model="OPENAI_MODEL_NAME")

# content blog senior researcher
blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video content for the topic {topic} from Youtube channel',
    verbose=True,
    memory=True, 
    backstory = (
        'Expert in understanding videos in AI Data Science, Machine Learning and GEN AI and providing suggestions'
    ),
    tools=[yt_tool],
    # llm = llm,
    allow_delegation=True
)

# senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from Youtube channel',
    verbose=True,
    memory=True, 
    backstory = (
        'With a flair for simplifying complex tools, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner.'
    ),
    tools=[yt_tool],
    # llm=llm,
    allow_delegation=False
)
import os
from textwrap import dedent

from crewai import Agent
from langchain_community.chat_models import BedrockChat

from helpers import CLAUDE_V3_SONNET_MODEL_ID, get_client
from tools import BrowserTools, SearchTools, create_ppt


class ContentResearcher:
    def __init__(self):
        client = get_client(
            access_key_id=os.getenv("BEDROCK_ACCESS_KEY_ID"),
            secret_access_key=os.getenv("BEDROCK_SECRET_ACCESS_KEY"),
            region=os.getenv("BEDROCK_REGION"),
        )
        self.llm = BedrockChat(
            client=client,
            model_id=CLAUDE_V3_SONNET_MODEL_ID,
            model_kwargs={
                "max_tokens": 8000,
            },
        )

    def get_agent(self):
        return Agent(
            role="Senior Content Researcher",
            goal=dedent(
                """\
                Search the web for information on the given topic and curate the content for a presentation."""
            ),
            backstory=dedent(
                """\
                As a Senior Content Researcher, you are responsible for researching and curating content on a given topic. You will use your expertise to search the web for relevant information for a presentation. You will be using the latest tools and technologies to gather information and present it in a clear and concise manner. Your goal is to provide valuable insights and knowledge to your audience.
				"""
            ),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
            ],
            allow_delegation=False,
            llm=self.llm,
            verbose=True,
        )


class ContentOutlineCreator:
    def __init__(self):
        client = get_client(
            access_key_id=os.getenv("BEDROCK_ACCESS_KEY_ID"),
            secret_access_key=os.getenv("BEDROCK_SECRET_ACCESS_KEY"),
            region=os.getenv("BEDROCK_REGION"),
        )
        self.llm = BedrockChat(
            client=client,
            model_id=CLAUDE_V3_SONNET_MODEL_ID,
            model_kwargs={
                "max_tokens": 8000,
            },
        )

    def get_agent(self):
        return Agent(
            role="Content Outline Creator",
            goal=dedent(
                """\
                Given the topic and its relevant information, create a well structured outline for a power point presentation.

                The outline should be in the format of slides, with main points, sub-points, and key takeaways from the topic.
                """
            ),
            backstory=dedent(
                """\
                As a Content Outline Creator, you are responsible for creating a structured outline for a power point presentation based on the given topic. You will use your expertise to organize the information in a logical and coherent manner. Your goal is to provide a clear and concise outline that will guide the presentation creation process. You will be using the latest tools and technologies to create an effective outline that will engage and inform the audience. 
				"""
            ),
            allow_delegation=False,
            llm=self.llm,
            verbose=True,
        )


class SeniorContentWriter:
    def __init__(self):
        client = get_client(
            access_key_id=os.getenv("BEDROCK_ACCESS_KEY_ID"),
            secret_access_key=os.getenv("BEDROCK_SECRET_ACCESS_KEY"),
            region=os.getenv("BEDROCK_REGION"),
        )
        self.llm = BedrockChat(
            client=client,
            model_id=CLAUDE_V3_SONNET_MODEL_ID,
            model_kwargs={
                "max_tokens": 8000,
            },
        )

    def get_agent(self):
        return Agent(
            role="Senior Content Writer",
            goal=dedent(
                """\
                Write a detailed and engaging content for the presentation based on the outline provided.
                    
                Fill in the outline with engaging and informative content that will captivate the audience.
                """
            ),
            backstory=dedent(
                """\
                As a Senior Content Writer, you are responsible for creating engaging and informative content for the presentation based on the outline provided. You will use your expertise to craft a detailed and well-structured content that will captivate the audience. Your goal is to provide valuable insights and knowledge on the topic in a compelling and engaging manner. You will be using the latest tools and technologies to create high-quality content that will resonate with the audience.
                """
            ),
            allow_delegation=False,
            llm=self.llm,
            verbose=True,
        )


class PresentationCreator:
    def __init__(self):
        client = get_client(
            access_key_id=os.getenv("BEDROCK_ACCESS_KEY_ID"),
            secret_access_key=os.getenv("BEDROCK_SECRET_ACCESS_KEY"),
            region=os.getenv("BEDROCK_REGION"),
        )
        self.llm = BedrockChat(
            client=client,
            model_id=CLAUDE_V3_SONNET_MODEL_ID,
            model_kwargs={
                "max_tokens": 8000,
            },
        )

    def get_agent(self):
        return Agent(
            role="Presentation Creator",
            goal=dedent(
                """\
                Create a visually appealing and engaging presentation based on the content provided.
                """
            ),
            backstory=dedent(
                """\
                As a Presentation Creator, you are responsible for creating a visually appealing and engaging presentation based on the content provided. You will use your expertise to design a presentation that is informative, engaging, and visually appealing. Your goal is to create a presentation that will captivate the audience and deliver the key messages effectively. You will be using the latest tools and technologies to create a high-quality presentation that will leave a lasting impression on the audience.
                """
            ),
            tools=[create_ppt],
            allow_delegation=False,
            llm=self.llm,
            verbose=True,
        )

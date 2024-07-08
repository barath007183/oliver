from crewai import Crew
from dotenv import load_dotenv

from agents import (ContentOutlineCreator, ContentResearcher,
                    PresentationCreator, SeniorContentWriter)
from tasks import (create_presentation, create_presentation_content,
                   create_presentation_outline, research_topic)


def main():
    load_dotenv()
    # agents
    senior_content_researcher = ContentResearcher().get_agent()
    content_outline_creator = ContentOutlineCreator().get_agent()
    senior_content_writer = SeniorContentWriter().get_agent()
    presentation_creator = PresentationCreator().get_agent()

    topic = input("Enter the topic you want to create a PPT for: ")

    # tasks
    research_topic_task = research_topic(senior_content_researcher, topic)
    create_presentation_outline_task = create_presentation_outline(
        content_outline_creator,
    )
    create_presentation_content_task = create_presentation_content(
        senior_content_writer
    )
    create_presentation_task = create_presentation(presentation_creator)

    # create a crew
    presentation_creation_crew = Crew(
        agents=[
            senior_content_researcher,
            content_outline_creator,
            senior_content_writer,
            presentation_creator,
        ],
        tasks=[
            research_topic_task,
            create_presentation_outline_task,
            create_presentation_content_task,
            create_presentation_task,
        ],
        verbose=True,
    )

    presentation_creation_crew.kickoff()


if __name__ == "__main__":
    main()

from textwrap import dedent

from crewai import Task


def research_topic(agent, topic):
    return Task(
        description=dedent(
            f"""\
            Analyze the given topic: {topic} and provide a detailed report on the topic.
            
            The content should be well-researched and should include relevant information on the topic. 
            The report should be informative, providing valuable insights and knowledge on the topic.
            This content will be used to create a presentation, keep that in mind while generating the report.

            Keep in mind, attention to detail is crucial for
			a comprehensive analysis. It's currenlty 2024.

            The report provided will be used to create a presentation on the topic.
			"""
        ),
        expected_output="A detailed report on the given topic.",
        agent=agent,
    )


def create_presentation_outline(agent):
    return Task(
        description=dedent(
            f"""\
            Given a topic and its relevant information, create a well-structured outline for a power point presentation.
            
            The outline should include the main points, sub-points, and key takeaways from the topic.
            The outline should be clear, concise, and well-organized, providing a roadmap for the presentation.
            The outline will be used to create a detailed presentation on the topic.
            """
        ),
        expected_output="A well-structured outline for a power point presentation.",
        agent=agent,
    )


def create_presentation_content(agent):
    return Task(
        description=dedent(
            f"""\
            Write a detailed and engaging content for the presentation based on the outline provided.
            
            Fill in the outline with engaging and informative content that will captivate the audience.
            The content should be well-researched and should provide valuable insights and knowledge on the topic.
            The content should be structured, coherent, and engaging, keeping the audience in mind.
            
            Important: Generate the complete content for the presentation. Do not leave any placeholders.
            """
        ),
        expected_output="Detailed and engaging content for the presentation.",
        agent=agent,
    )


def create_presentation(agent):
    return Task(
        description=dedent(
            """\
            Create a PPT presentation based on the content provided.
            
            Use the outline to structure the presentation and the content to fill in the details.
            The presentation should be engaging, informative, and visually appealing.
            
            The presentation should flow logically, guiding the audience through the topic.

            You have access to three types of slides:
            1. title_slide - Just the title can be used for the first slide.
            2. section_header - Title with a section header can be used for section titles. i.e. Introduction, Conclusion etc
            3. content_slide - Title with content can be used for main content slides.

            Important Note - When you are adding content to the slides, It should be in html format. Format the content accordingly.
            """
        ),
        expected_output="A PPT presentation based on the content.",
        agent=agent,
    )

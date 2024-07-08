## Oliver - A simple pptx generator using AI Agents

### What does Oliver do?

1. You provide Oliver with a topic to generate a pptx presentation.
2. Searches the web for relevant information on the topic.
3. Comes with a outline of the presentation based on the information found.
4. Generates content for each slide.
5. Creates a pptx presentation with the content.

### How to setup

1. Clone the repository
2. We use poetry for managing dependencies. Install [Poetry](https://python-poetry.org/docs/#installation)
3. Run `poetry install` to install the dependencies
4. Copy the `.env.example` file to `.env` and fill in the required values
5. Run `poetry shell` to activate the virtual environment
6. Run `python -m oliver` to start the program

### How is the code structured?

1. `oliver.py` - The main entry point for the program.
2. `agents.py` - Contains the AI agents that are used to generate the content.
3. `tasks.py` - Contains the tasks that are executed by the agents.
4. `tools.py` - Contains the tools that are used by the agents in order to complete their tasks.
5. `helpers.py` - Contains helper functions.

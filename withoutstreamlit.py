from agno.agent import Agent
from agno.storage.sqlite import SqliteStorage
from agno.tools.youtube import YouTubeTools
from agno.models.google import Gemini
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp", api_key='AIzaSyDWUk0f_nYQ2NDUHWKfmDquUbMeCozXs-g'),
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
    # Fix the session id to continue the same session across execution cycles
    session_id="fixed_id_for_demo",
    storage=SqliteStorage(table_name="agent_sessions", db_file="tmp/data.db"),
    add_history_to_messages=True,
    num_history_runs=3,
    tools=[YouTubeTools()]
)
while True:
    # Get user input
    user_input = input("You: ")
    # Check if the user wants to exit
    if user_input.lower() in ["exit", "quit", "q"]:
        break
    # Get the agent's response
    agent.print_response(user_input)
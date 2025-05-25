
from agno.agent import Agent
from agno.storage.sqlite import SqliteStorage
from agno.tools.youtube import YouTubeTools
from agno.models.google import Gemini
def agent_int():
    ag =  Agent(
        model=Gemini(id="gemini-2.0-flash-exp", api_key='Your API Key'),
        description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
        session_id="streamlit_session",
        storage=SqliteStorage(table_name="agent_sessions", db_file="tmp/data.db"),
        add_history_to_messages=True,
        num_history_runs=20,
        tools=[YouTubeTools()],
        show_tool_calls=True,
    )
    return ag

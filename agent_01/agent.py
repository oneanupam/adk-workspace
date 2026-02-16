# Import the agent class from the google adk
from google.adk.agents.llm_agent import Agent

# Main agent that ADK will look for when running the agent
root_agent = Agent(
    model='gemini-2.5-flash', # Model: The reasoning engine that the agent will use to answer questions. This should be a model that is supported by the ADK.
    name='root_agent',  # Identity: Required identifier for the agent
    description='A helpful assistant for user questions.', # Purpose: What this agent does
    instruction='Answer user questions to the best of your knowledge', # Behavior: How to act means how the agent should behave
    # Tools: Can be added based on the needs of the agent. Tools are used to augment the capabilities of the agent and can be used for things like web search, calculations, etc.
    # Orchestration: Handled automatically by the Agent class. The Agent class automatically runs the "Perceive → Think → Act → Check" loop
)

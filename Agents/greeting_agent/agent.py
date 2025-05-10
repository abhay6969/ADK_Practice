from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    description="A Simple Greeting Agent",
    model="gemini-2.0-flash",
    instruction="""You are a helpful assistant that greets the user.
    Ask for the user's name and greet them by name."""
)
from myfirstaios.agent import PersonalAgent


def test_agent_creation():
    agent = PersonalAgent()
    assert agent.name == "PersonalAgent"


def test_tool_call_placeholder():
    agent = PersonalAgent()
    result = agent.run_tool("echo", "hello")
    assert "echo" in result or "not implemented" in result.lower()

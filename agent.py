import json

from llm import ask_llm
from tools.calculator import calculate
from tools.knowledge import search_knowledge
from tools.quiz import create_quiz_prompt


SYSTEM_PROMPT = """
You are an AI Study Assistant Agent.

You have access to three tools:

1. calculator
   Use it for mathematical calculations.

2. knowledge
   Use it when the user asks about topics
   that may exist in the study knowledge base.

3. quiz
   Use it when the user asks for MCQs,
   quizzes, or practice questions.

Decide which tool is appropriate.

Return ONLY valid JSON.

For a tool call:

{
    "action": "tool",
    "tool": "calculator",
    "input": "25 * 40"
}

For knowledge:

{
    "action": "tool",
    "tool": "knowledge",
    "input": "object oriented programming"
}

For quiz:

{
    "action": "tool",
    "tool": "quiz",
    "input": "Python, 5"
}

If no tool is needed:

{
    "action": "answer",
    "input": "your answer"
}
"""


def decide_action(user_message):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_message
        }
    ]

    response = ask_llm(messages)

    try:
        return json.loads(response)

    except json.JSONDecodeError:
        return {
            "action": "answer",
            "input": response
        }


def execute_tool(tool, tool_input):

    if tool == "calculator":
        return calculate(tool_input)

    if tool == "knowledge":
        return search_knowledge(tool_input)

    if tool == "quiz":

        parts = tool_input.split(",")

        topic = parts[0].strip()

        number = 5

        if len(parts) > 1:
            try:
                number = int(parts[1].strip())
            except ValueError:
                number = 5

        return create_quiz_prompt(
            topic,
            number
        )

    return "Unknown tool."


def run_agent(user_message):

    decision = decide_action(user_message)

    if decision["action"] == "answer":

        return decision["input"]

    if decision["action"] == "tool":

        tool = decision["tool"]

        tool_input = decision["input"]

        tool_result = execute_tool(
            tool,
            tool_input
        )

        final_messages = [
            {
                "role": "system",
                "content": """
You are an AI Study Assistant.

Answer the user's question using the
tool result provided.

Do not mention internal tools.
Give a clear educational answer.
"""
            },
            {
                "role": "user",
                "content": user_message
            },
            {
                "role": "assistant",
                "content": f"Tool result:\n{tool_result}"
            }
        ]

        return ask_llm(final_messages)

    return "I could not determine what action to take."
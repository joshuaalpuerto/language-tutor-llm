SYSTEM_PROMPT = """[INST]You are a cool {language} teacher and having a 1-on-1 session with your student who is an english speaker.

You must follow the guidelines below when responding:
- Use the session history to continue the conversation. If its empty ask the student about any topic they want to share.
- Only reply in {language} and once you are finish provide an English translation of the response in (parenthesis).
- You MUST provide your correction or reasoning on any mistake on grammar or typo on their message before replying. 

>>> Session history
{chat_history}

>>> Student last message
{input}[/INST]"""


DEFAULT_SUMMARIZER_TEMPLATE = """[INST]Progressively summarize the lines of conversation provided, adding onto the previous summary returning a new summary.

EXAMPLE
Current summary:
The human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good.

New lines of conversation:
Human: Why do you think artificial intelligence is a force for good?
AI: Because artificial intelligence will help humans reach their full potential.

New summary:
The human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good because it will help humans reach their full potential.
END OF EXAMPLE

Current summary:
{summary}

New lines of conversation:
{new_lines}

New summary:[/INST]"""
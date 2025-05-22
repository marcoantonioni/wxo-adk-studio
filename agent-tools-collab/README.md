# Multilanguage greeter
This example explain how to create a collaboration with multiple tools.
Each tool is designed to answer in a specific language.
The query in a specific language drive the agent to select the most appropriate tool.
Each tool has a detailed description in its own language.

## Steps to import
1. Run `orchestrate server start -e .your-env`
2. Run `./import-all.sh`
3. Run `orchestrate chat start`
4. Select from agents 'agent_tool_collab'
5. New Chat

## Suggested script
- you say: Ciao

- you say: Buongiorno

- you say: I'm from London
-- agent answer: What language do you want to use for greetings?
--- you say: english

- you say: Good morning

- you say: Buenas dia

- you say: Hola

- you say: Guten Morgen
-- agent answer: What language do you want to use for greetings?
--- you say: german
---- agent answer: I don't have a function for german greeter available.

See 'Reasoning' twist and Steps with proper Tool selection.
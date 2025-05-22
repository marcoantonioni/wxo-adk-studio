# Multilanguage greeter
This example explain how to create a collaboration among an agent and multiple tools.
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
Answers may change based on the LLM model.<br>
use: watsonx/meta-llama/llama-3-2-90b-vision-instruct

- you say: Ciao<br>

- you say: Buongiorno<br>

- you say: I'm from London<br>
-- agent answer: What language do you want to use for greetings?<br>
--- you say: english<br>

- you say: Good morning<br>

- you say: Buenas dia<br>

- you say: Hola<br>

- you say: Guten Morgen<br>
-- agent answer: What language do you want to use for greetings?<br>
--- you say: german<br>
---- possible agent answer: I don't have a function for german greeter available.<br>
---- possible agent answer: I don't have a function for German greetings. I can only respond with greetings in Italian, English, or Spanish. Would you like to try one of those languages?<br>


See 'Reasoning' twist and Steps with proper Tool selection.
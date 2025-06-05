# Chat text to tool input params
This example explain how to the text from chat can be used as tool input parameter.

## Steps to import
1. Run `orchestrate server start -e .your-env`
2. Run `./import-all.sh`
3. Run `orchestrate chat start`
4. Select from agents 'MA42021_agent_tool_chat_inputs'
5. New Chat

## Suggested script
Answers may change based on the LLM model.<br>
use: watsonx/meta-llama/llama-3-2-90b-vision-instruct

- you say: My first name is Marco, my last name is Antonioni, give me my full name.<br>
-- agent answer: Your full name is Marco Antonioni.

- you say: My first name is James, my last name is Bond, give me my full name.<br>
-- agent answer: Your full name is Marco Antonioni.

- you say: My name is Johnny, some one call me by last name and says Stecchino, give me my full name.<br>
-- agent answer: Your full name is Johnny Stecchino.

- you say: Give me my full name
-- agent answer: What is your first name?
--- you say: Marco 
---- agent answer: What is your last name?
----- you say: Antonioni 
------ agent answer: Your fullname is Marco Antonioni

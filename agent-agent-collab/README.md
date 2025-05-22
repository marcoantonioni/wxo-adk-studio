# Multi agent collaboration
This example explain how to create a collaboration among agents (main and sub).
Each sub agent is designed to answer about a specific topic (history and geography).
The query containing 'a topic' drive the main agent to select the most appropriate sub agent.
Each sub agent has a dedicate tool to produce the answer.

## Steps to import
1. Run `orchestrate server start -e .your-env`
2. Run `./import-all.sh`
3. Run `orchestrate chat start`
4. Disable 'Show agent' check in 'Manage agents' for both sub agents 'MA42021_agent_geography' and 'MA42021_agent_history'.
4. Select from agents 'MA42021_agent_agent_collab'
5. New Chat

## Suggested script
Answers may change based on the LLM model.<br>
use: watsonx/meta-llama/llama-3-2-90b-vision-instruct

- you say: I want know about topic history<br>

- you say: I want know about topic geography<br>
  (*) if done in the same chat note the return to the supervisor agent<br>
      Step 1<br>
        Tool : transfer_to_supervisor<br>

- you say: I want know about topic chemistry<br>
-- agent answer: What is the topic?<br>
--- you say: chemistry<br>
---- agent answer: I don't have information about chemistry. I can help you with history or geography. Which one would you like to know more about?


See 'Reasoning' twist and Steps with proper SubAgent/Tool selection.
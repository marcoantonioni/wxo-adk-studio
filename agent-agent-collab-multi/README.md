# Multi agent collaboration

## Steps to import
1. Run `orchestrate server start -e .your-env`
2. Run `./import-all.sh`
3. Run `orchestrate chat start`
4. Disable 'Show agent' check in 'Manage agents' for sub agents ....
4. Select from agents 'MA42021_agent_agent_collab_multi'
5. New Chat

## Suggested script
Answers may change based on the LLM model.<br>
use: watsonx/meta-llama/llama-3-2-90b-vision-instruct

- you say: give me the personal informations, purchase transactions and loyalties informations of customer Marco<br>

- you say: give me the first name, age and address of customer Marco<br>



See 'Reasoning' twist and Steps with proper SubAgent/Tool selection.
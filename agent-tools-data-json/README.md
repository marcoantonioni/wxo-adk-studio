# Chat text to tool input params
This example explain how to the text from chat can be used as tool input parameter.

## Steps to import
1. Run `orchestrate server start -e .your-env`
2. Run `./import-all.sh`
3. Run `orchestrate chat start`
4. Select from agents 'MA42021_agent_tool_data_json'
5. New Chat

## Suggested script
Answers may change based on the LLM model.<br>
use: watsonx/meta-llama/llama-3-2-90b-vision-instruct<br>
note: the tool return the name of city in UPPERCASE format and the date time in which the request has been issued

- you say: give the weather forecast for Trieste for date 08/15/2026<br>
-- agent answer: The weather forecast for Trieste on August 15, 2026, is 26 degrees.

- you say: give the weather forecast for Trieste for date 08/15/2026, for the answer data you must use the name of city and the date and time in which the request has been issued from tool results<br>
-- agent answer: The weather forecast for TRIESTE on August 15, 2026, is -4 degrees.


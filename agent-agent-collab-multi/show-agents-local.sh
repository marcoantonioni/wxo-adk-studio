#!/bin/bash

export WXO_TOKEN_LOCAL=$(cat ~/.cache/orchestrate/credentials.yaml | yq .auth.local.wxo_mcsp_token)

AGENT_NAME=MA42021_agent_customer_personal_informations
AGENT_ID=$(curl -s -H 'Content-Type: application/json' -H 'accept: application/json' -H 'Authorization: Bearer '${WXO_TOKEN_LOCAL} -X 'GET' 'http://localhost:4321/api/v1/orchestrate/agents?include_hidden=true&names='${AGENT_NAME} | jq .[0].id | sed 's/"//g')
curl -s -X 'PATCH' http://localhost:4321/api/v1/orchestrate/agents/${AGENT_ID} -H 'Content-Type: application/json' -H 'accept: application/json' -H 'Authorization: Bearer '${WXO_TOKEN_LOCAL} -d '{"hidden": false}'

AGENT_NAME=MA42021_agent_customer_loyalty_informations
AGENT_ID=$(curl -s -H 'Content-Type: application/json' -H 'accept: application/json' -H 'Authorization: Bearer '${WXO_TOKEN_LOCAL} -X 'GET' 'http://localhost:4321/api/v1/orchestrate/agents?include_hidden=true&names='${AGENT_NAME} | jq .[0].id | sed 's/"//g')
curl -s -X 'PATCH' http://localhost:4321/api/v1/orchestrate/agents/${AGENT_ID} -H 'Content-Type: application/json' -H 'accept: application/json' -H 'Authorization: Bearer '${WXO_TOKEN_LOCAL} -d '{"hidden": false}'

AGENT_NAME=MA42021_agent_customer_transactions_informations
AGENT_ID=$(curl -s -H 'Content-Type: application/json' -H 'accept: application/json' -H 'Authorization: Bearer '${WXO_TOKEN_LOCAL} -X 'GET' 'http://localhost:4321/api/v1/orchestrate/agents?include_hidden=true&names='${AGENT_NAME} | jq .[0].id | sed 's/"//g')
curl -s -X 'PATCH' http://localhost:4321/api/v1/orchestrate/agents/${AGENT_ID} -H 'Content-Type: application/json' -H 'accept: application/json' -H 'Authorization: Bearer '${WXO_TOKEN_LOCAL} -d '{"hidden": false}'

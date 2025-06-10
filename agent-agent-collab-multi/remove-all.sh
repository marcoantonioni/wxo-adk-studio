#!/usr/bin/env bash
set -x

orchestrate agents remove  -k native -n MA42021_agent_agent_collab_multi
orchestrate agents remove  -k native -n MA42021_agent_customer_personal_informations
orchestrate agents remove  -k native -n MA42021_agent_customer_loyalty_informations
orchestrate agents remove  -k native -n MA42021_agent_customer_transactions_informations
orchestrate tools remove -n MA42021_tool_customer_personal_informations
orchestrate tools remove -n MA42021_tool_customer_loyalty_informations
orchestrate tools remove -n MA42021_tool_customer_purchase_transactions


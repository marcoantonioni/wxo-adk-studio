#!/usr/bin/env bash
set -x

orchestrate agents remove  -k native -n MA42021_agent_tool_connection
orchestrate tools remove -n MA42021_tool_connection

APP_ID=CONN_TC
orchestrate connections remove --app-id $APP_ID

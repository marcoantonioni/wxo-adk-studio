#!/usr/bin/env bash
set -x

orchestrate agents remove  -k native -n MA42021_agent_tool_collab
orchestrate tools remove -n MA42021_greeter_italian
orchestrate tools remove -n MA42021_greeter_english
orchestrate tools remove -n MA42021_greeter_spanish


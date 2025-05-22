#!/usr/bin/env bash
set -x

# orchestrate env activate local
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

orchestrate agents remove  -k native -n MA42021_agent_tool_collab
orchestrate tools remove -n MA42021_greeter_italian
orchestrate tools remove -n MA42021_greeter_english
orchestrate tools remove -n MA42021_greeter_spanish


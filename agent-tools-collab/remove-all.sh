#!/usr/bin/env bash
set -x

orchestrate env activate local
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

orchestrate agents remove  -k native -n agent_tool_collab
orchestrate tools remove -n greeter_italian
orchestrate tools remove -n greeter_english
orchestrate tools remove -n greeter_spanish


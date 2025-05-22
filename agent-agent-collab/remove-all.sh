#!/usr/bin/env bash
set -x

# orchestrate env activate local
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

orchestrate agents remove  -k native -n MA42021_agent_agent_collab
orchestrate agents remove  -k native -n MA42021_agent_geography
orchestrate agents remove  -k native -n MA42021_agent_history
orchestrate tools remove -n MA42021_topic_geography
orchestrate tools remove -n MA42021_greeter_english
orchestrate tools remove -n MA42021_topic_history


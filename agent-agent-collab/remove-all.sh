#!/usr/bin/env bash
set -x

orchestrate agents remove  -k native -n MA42021_agent_agent_collab
orchestrate agents remove  -k native -n MA42021_agent_geography
orchestrate agents remove  -k native -n MA42021_agent_history
orchestrate tools remove -n MA42021_topic_geography
orchestrate tools remove -n MA42021_greeter_english
orchestrate tools remove -n MA42021_topic_history


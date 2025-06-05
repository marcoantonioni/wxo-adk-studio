#!/usr/bin/env bash
set -x

orchestrate agents remove  -k native -n MA42021_agent_tool_data_json
orchestrate tools remove -n MA42021_tool_weather_forecast


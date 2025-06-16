#!/usr/bin/env bash
set -x

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

APP_ID=CONN_TC
orchestrate connections remove --app-id $APP_ID
orchestrate connections add --app-id $APP_ID
orchestrate connections import --file ${SCRIPT_DIR}/connection.yaml

# Set credentials
APP_USERNAME=marco
APP_PASSWORD=passw0rd
orchestrate connections set-credentials --app-id $APP_ID --env draft --username $APP_USERNAME --password $APP_PASSWORD

for python_tool in ./*.py; do
  orchestrate tools import -k python -f ${SCRIPT_DIR}/${python_tool} --app-id $APP_ID
done

orchestrate agents import -f ${SCRIPT_DIR}/agent.yaml


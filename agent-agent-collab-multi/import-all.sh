#!/usr/bin/env bash
set -x


# orchestrate env activate local
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

${SCRIPT_DIR}/show-agents-local.sh

for python_tool in ./*.py; do
  orchestrate tools import -k python -f ${SCRIPT_DIR}/${python_tool}
done

orchestrate agents import -f ${SCRIPT_DIR}/agent-cust-info.yaml
orchestrate agents import -f ${SCRIPT_DIR}/agent-cust-loyalty.yaml
orchestrate agents import -f ${SCRIPT_DIR}/agent-cust-transactions.yaml
orchestrate agents import -f ${SCRIPT_DIR}/agent.yaml

${SCRIPT_DIR}/hide-agents-local.sh


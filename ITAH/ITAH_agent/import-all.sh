# Create rapid api connection
orchestrate connections add --app-id ITAH
orchestrate connections import --file './connections/itah.yaml'

# Set credentials
ITAH_USERNAME=$(grep '^ITAH_USERNAME[[:space:]]*=' creds.txt | sed 's/^[^=]*=[[:space:]]*//')
ITAH_PASSWORD=$(grep '^ITAH_PASSWORD[[:space:]]*=' creds.txt | sed 's/^[^=]*=[[:space:]]*//')
#echo "<$ITAH_USERNAME>"
#echo "<$ITAH_PASSWORD>"
orchestrate connections set-credentials --app-id ITAH --env draft --username $ITAH_USERNAME --password $ITAH_PASSWORD

# Import tools that have connection requirements
orchestrate tools import \
 -k python \
 -f './tools/get_orders_by_user.py' \
 -a ITAH
orchestrate tools import \
 -k python \
 -f './tools/get_order_status.py' \
 -a ITAH
orchestrate tools import \
 -k python \
 -f './tools/create_sample_orders.py' \
 -a ITAH
orchestrate tools import \
 -k python \
 -f './tools/cleanup_user_orders.py' \
 -a ITAH 
#orchestrate tools import \
# -k openapi \
# -f './tools/ITAH_agent_tools.yaml' \
# -a ITAH
 
# Import agents
orchestrate agents import -f './agents/ITAH_agent.yaml'


read -p "Press enter to continue"

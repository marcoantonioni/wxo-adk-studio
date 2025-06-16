export ITAH_USERNAME=$(grep '^ITAH_USERNAME[[:space:]]*=' creds.txt | sed 's/^[^=]*=[[:space:]]*//')
export ITAH_PASSWORD=$(grep '^ITAH_PASSWORD[[:space:]]*=' creds.txt | sed 's/^[^=]*=[[:space:]]*//')
export ITAH_URL=$(grep '^ITAH_URL=' creds.txt | sed 's/^ITAH_URL=//')

curl -u $ITAH_USERNAME:$ITAH_PASSWORD \
     -X POST $ITAH_URL/ITAH_CleanupUserOrders \
     -H "Content-Type: application/json" \
     -k \
     -d '{"userEmail":"usr001"}' > temp.json

read -p "Press enter to continue"
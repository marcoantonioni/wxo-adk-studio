# Create rapid api connection
orchestrate connections remove --app-id ITAH
orchestrate tools remove -n cleanup_user_orders
orchestrate tools remove -n create_sample_orders
orchestrate tools remove -n get_orders_by_user
orchestrate tools remove -n get_order_status
orchestrate agents remove -n ITAH_agent -k native

read -p "Press enter to continue"
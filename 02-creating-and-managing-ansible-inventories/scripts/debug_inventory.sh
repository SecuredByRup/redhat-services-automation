#!/bin/bash

INVENTORY_FILE=$1

if [ -z "$INVENTORY_FILE" ]; then
    echo "Usage: $0 <inventory_file>"
    exit 1
fi

echo "=== Inventory Debug Report ==="
echo "Inventory file: $INVENTORY_FILE"
echo "Generated on: $(date)"
echo

echo "=== Inventory Structure ==="
ansible-inventory -i "$INVENTORY_FILE" --graph
echo

echo "=== All Hosts ==="
ansible-inventory -i "$INVENTORY_FILE" --list | python3 -c "import sys, json; data=json.load(sys.stdin); print('\n'.join(data.get('_meta', {}).get('hostvars', {}).keys()))"
echo

echo "=== Connectivity Test ==="
ansible all -i "$INVENTORY_FILE" -m ping --one-line
echo

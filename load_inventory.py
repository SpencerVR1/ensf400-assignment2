import ansible_runner
import subprocess

def get_inventory():
    action = 'list'
    inventory_path = ['hosts.yml']
    inventory_data, error = ansible_runner.get_inventory(action, inventory_path, response_format='json')

    if error:
        print(f"Error: {error}")
        exit(1)

    for group, hosts_obj in inventory_data.items():
        if group != '_meta' and group != 'all':
            hosts_list = hosts_obj['hosts']
            for host in hosts_list:
                print("Host: " + host)
                host_info = inventory_data['_meta']['hostvars'][host]
                if len(host_info) > 1:
                    ip = inventory_data['_meta']['hostvars'][host]['ansible_host']
                    print("IP Address: " + ip)
                else:
                    print("IP Address: Local")
                print("Group Name: " + group)
                print()

def ping_hosts():
    subprocess.run(['export', 'ANSIBLE_CONFIG=$(pwd)/ansible.cfg'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    result = subprocess.run(['ansible', 'all:localhost', '-m', 'ping'], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    get_inventory()
    ping_hosts()
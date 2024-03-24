import ansible_runner
import requests

def run_playbook():
    r = ansible_runner.run(private_data_dir='.', playbook='hello_from_lab.yml', host_pattern='app')
    print("Status:", r.status)
    print("Return Code:", r.rc)
    print()

    try:
        response = requests.get("http://0.0.0.0:3000/")
        if response.status_code == 200:
            print(f"response from http://0.0.0.0:3000/: {response.text}")
        else:
            print(f"Error from http://0.0.0.0:3000/: {response.status_code}")


        response = requests.get("http://0.0.0.0:3001/")
        if response.status_code == 200:
            print(f"response from http://0.0.0.0:3001/: {response.text}")
        else:
            print(f"Error from http://0.0.0.0:3001/: {response.status_code}")


        response = requests.get("http://0.0.0.0:3002/")
        if response.status_code == 200:
            print(f"response from http://0.0.0.0:3002/: {response.text}")
        else:
            print(f"Error from http://0.0.0.0:3002/: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error fetching a URL: {e}")

if __name__ == "__main__":
    run_playbook()
import subprocess

# command = f"az group export --name Automation-new-env --output json > template10.json"

command = f"az storage account show-connection-string --resource-group Automation-new-env --name storagenewenvpsh1708 --output tsv"

result = subprocess.run(command, shell=True, capture_output=True, text=True)

connection_string = result.stdout

string_list = connection_string.split(';')

priority_order = {"DefaultEndpointsProtocol": 1, "AccountName": 2, "AccountKey": 3,"EndpointSuffix":4}

filtered_list = sorted(
    [item for item in string_list if any(key in item for key in priority_order)],
    key=lambda item: min(priority_order[key] for key in priority_order if key in item)
)
account_key = filtered_list[2].replace("AccountKey=","")

final_connection_string = ';'.join(filtered_list)

print("Final String",final_connection_string)
print("Account_key",account_key)

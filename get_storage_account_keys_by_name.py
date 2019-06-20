import os

from cloud.azure_service import AzureService

def main():
    """Execute script."""

    azure_service = AzureService()
    resource_group_name = os.environ.get('RESOURCE_GROUP_NAME', 'costmgmt')
    storage_account_name = os.environ.get(
        'STORAGE_ACCOUNT', 'costmgmtacct1234')
    storage_account_keys = azure_service.get_storage_account_keys(
        resource_group_name, storage_account_name)
    key_count = len(storage_account_keys.keys)
    print(f'Found {key_count} keys for storage account {storage_account_name}')
    for key in storage_account_keys.keys:
        print(f'{key.key_name}={key.value}')

main()

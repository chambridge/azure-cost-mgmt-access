import os

from cloud.azure_service import AzureService

def main():
    """Execute script."""

    azure_service = AzureService()
    resource_group_name = os.environ.get('RESOURCE_GROUP_NAME', 'costmgmt')
    storage_account_name = os.environ.get(
        'STORAGE_ACCOUNT', 'costmgmtacct1234')
    storage_account = azure_service.get_storage_account(
        resource_group_name, storage_account_name)
    print(f'storage_account.id={storage_account.id}')

main()

import os

from cloud.azure_service import AzureService

def main():
    """Execute script."""

    azure_service = AzureService()
    resource_group_name = os.environ.get('RESOURCE_GROUP_NAME', 'costmgmt')
    storage_account_name = os.environ.get(
        'STORAGE_ACCOUNT', 'costmgmtacct1234')
    container_name = os.environ.get('STORAGE_CONTAINER', 'cur')
    storage_account_container = azure_service.get_storage_account_container(
        resource_group_name, storage_account_name, container_name)
    print(f'storage_account_container.id={storage_account_container.id}')

main()

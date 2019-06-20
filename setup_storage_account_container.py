import os

from cloud.azure_service import AzureService

def main():
    """Execute script."""
    resource_group_name = os.environ.get('RESOURCE_GROUP_NAME', 'costmgmt')
    storage_account_name = os.environ.get(
        'STORAGE_ACCOUNT', 'costmgmtacct1234')
    container_name = os.environ.get('STORAGE_CONTAINER', 'cur')
    azure = AzureService()
    azure.create_storage_account_container(resource_group_name,
                                           storage_account_name, container_name)
    print(
        f'Storage account container {container_name} in {storage_account_name} was created.')


main()

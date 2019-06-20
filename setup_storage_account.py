import os

from cloud.azure_service import AzureService

def main():
    """Execute script."""
    resource_group_name = os.environ.get('RESOURCE_GROUP_NAME', 'costmgmt')
    region = os.environ.get('REGION', 'northcentralus')
    storage_account_name = os.environ.get(
        'STORAGE_ACCOUNT', 'costmgmtacct1234')
    azure = AzureService()
    azure.create_storage_account(resource_group_name,
                                 storage_account_name, region)
    print(f'Storage account {storage_account_name} was created.')


main()

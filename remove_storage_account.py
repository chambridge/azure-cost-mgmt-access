import os

from cloud.azure_service import AzureService


def main():
    """Execute script."""
    resource_group_name = os.environ.get('RESOURCE_GROUP_NAME', 'costmgmt')
    storage_account_name = os.environ.get(
        'STORAGE_ACCOUNT', 'costmgmtacct1234')
    azure = AzureService()

    azure.delete_storage_account(resource_group_name, storage_account_name)


main()

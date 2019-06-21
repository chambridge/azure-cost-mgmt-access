import os

from cloud.azure_service import AzureService

def main():
    """Execute script."""

    azure_service = AzureService()
    resource_group_name = os.environ.get('RESOURCE_GROUP_NAME', 'costmgmt')
    storage_account_name = os.environ.get(
        'STORAGE_ACCOUNT', 'costmgmtacct1234')
    container_name = os.environ.get('STORAGE_CONTAINER', 'cur')
    storage_account_blobs = azure_service.list_storage_account_container_blobs(
        resource_group_name, storage_account_name, container_name)
    blob_count = len(storage_account_blobs.items)
    print(
        f'Found {blob_count} blobs for storage account container {container_name}')
    for blob in storage_account_blobs:
        print(f'{blob.name} = {blob.properties.etag} - {blob.properties.last_modified}')

main()

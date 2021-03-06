import os

from cloud.azure_service import AzureService

def main():
    """Execute script."""
    resource_group_name = os.environ.get('RESOURCE_GROUP_NAME', 'costmgmt')
    region = os.environ.get('REGION', 'northcentralus')
    azure = AzureService()
    resource_group = azure.create_resource_group(resource_group_name, region)
    print(f'Resource group {resource_group_name} was created.')


main()

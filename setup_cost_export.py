import os

from cloud.azure_service import AzureService

def main():
    """Execute script."""
    resource_group_name = os.environ.get('RESOURCE_GROUP_NAME', 'costmgmt')
    storage_account_name = os.environ.get(
        'STORAGE_ACCOUNT', 'costmgmtacct1234')
    container_name = os.environ.get('STORAGE_CONTAINER', 'cur')
    export_name = os.environ.get('COST_REPORT', 'costreport')
    azure_service = AzureService()
    azure_service.create_cost_management_export(
        export_name=export_name,
        resource_group_name=resource_group_name,
        storage_account_name=storage_account_name,
        container_name=container_name
    )
    print(f'Daily scheduled cost report export {export_name} was created.')


main()

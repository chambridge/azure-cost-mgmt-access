import csv
import os

from cloud.azure_service import AzureService

def main():
    """Execute script."""

    azure_service = AzureService()
    resource_group_name = os.environ.get('RESOURCE_GROUP_NAME', 'costmgmt')
    storage_account_name = os.environ.get(
        'STORAGE_ACCOUNT', 'costmgmtacct1234')
    container_name = os.environ.get('STORAGE_CONTAINER', 'cur')
    export_name = os.environ.get('COST_REPORT', 'costreport')
    blob = azure_service.get_latest_cost_export(
        resource_group_name, storage_account_name, container_name, export_name)
    print(f'{blob.name} = {blob.properties.etag} - {blob.properties.last_modified}')

    file_path = azure_service.download_latest_cost_export(
        resource_group_name, storage_account_name, container_name, export_name)
    print(f'file_path={file_path}')
    
    with open(file_path) as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        print('First 3 rows.')
        row_count = 0
        for row in read_csv:
            print(row)
            row_count = row_count + 1
            if row_count >= 3:
                break

main()

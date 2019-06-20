import os

from cloud.azure_service import AzureService

def main():
    """Execute script."""
    azure_service = AzureService()
    export = azure_service.list_cost_management_export()
    export_count = len(export.value)
    print(f'Found {export_count} exports.')
    for export_report in export.value:
        print(f'export_report={export_report.id}')

main()

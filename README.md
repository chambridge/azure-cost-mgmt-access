# azure-cost-mgmt-access
Proof of concept code to setup an cost mgmt data extraction and pull data file.

## Background
The sample code here is meant to setup a daily cost export as described in this [Azure tutorial](https://docs.microsoft.com/en-us/azure/cost-management/tutorial-export-acm-data) and provide code to extract and read the cost report data once downloaded.

## Getting Started

1. Clone the repository:
```
git clone https://github.com/chambridge/azure-cost-mgmt-access.git
```

2. Setup virtual environment with _pipenv_
```
cd azure-cost-mgmt-access
pipenv install
```

3. Create a service principal
Follow the steps in the following Azure document to [create a service principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal)

Add the following roles to the service principal as described in the tutorial mentioned in *Background*: _Owner_, _Contributor_, and _Reader_.


4. Set environment variables
Copy the `.env.example` file to `.env` and provide the necessary variables.
```
cp ./.env.example ./.env
```

5. Enter virtual environment shell with set environment variables
```
pipenv shell
```

## Code Structure

Currently, the code to interact with Azure resides in the `cloud` directory. Outside of this there are several single purpose scripts to work with resource groups, storage accounts, storage account containers, and cost export. These scripts can be called directedly as seen in the following example:

```
python setup_resource_group.py
```
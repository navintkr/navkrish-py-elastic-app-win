import logging

import azure.functions as func
from key_vault_sample_base import KeyVaultSampleBase, keyvaultsample, get_name, run_all_samples
from azure.common.credentials import ServicePrincipalCredentials
from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.keyvault import KeyVaultId


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

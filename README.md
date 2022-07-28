# Azure Container Apps Album API

## Env Variables Powershell

$RESOURCE_GROUP="containerapps-demo"
$LOCATION="eastus"
$ENVIRONMENT="containerapps-env-demo"
$API_NAME="album-api"
$FRONTEND_NAME="album-ui"
$ACR_NAME="academo"

## ACR Build Command

cd into the src folder

az acr build --registry $ACR_NAME --image $API_NAME .

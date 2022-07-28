# Azure Container Apps Album API

## Env Variables

$RESOURCE_GROUP="containerapps-demo"
$LOCATION="eastus"
$ENVIRONMENT="containerapps-env-demo"
$API_NAME="album-api"
$FRONTEND_NAME="album-ui"
$ACR_NAME="academo"

## ACR Build Command

az acr build --registry $ACR_NAME --image $API_NAME .

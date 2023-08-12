import azure.functions as func
import logging
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpTrigger")
def HttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

 
    # Perform a GET request to the desired domain
    url = 'https://40268037selectfood.azurewebsites.net/return_foods'
    response = requests.get(url)

    # Check the response
    if response.status_code == 200:
        return func.HttpResponse(response.text, status_code=200)
    else:
        return func.HttpResponse("Failed to fetch data from the domain.", status_code=500)
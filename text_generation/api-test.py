import requests, time, logging, sys
API_ENDPOINT = "http://localhost:7071/api/orchestrators/orchestrator-generation-test"

def send_text(prompt, API_ENDPOINT):
    logging.info("Sending prompt")
    message = {"prompt": prompt}
    response = requests.post(API_ENDPOINT, json=message)
    return response

def get_links(response):
    body = response.json()
    # 'id'
    # 'statusQueryGetUri'
    # 'sendEventPostUri'
    # 'terminatePostUri'
    # 'rewindPostUri'
    # 'purgeHistoryDeleteUri'
    # 'restartPostUri'
    logging.info(f"Request Id: {body['id']}")
    return body['id'], body['statusQueryGetUri'], body['terminatePostUri']

def check_status(status):
    logging.info("Checking status")
    status_response = requests.get(status)
    body = status_response.json()
    if status_response.status_code == 202 and body['runtimeStatus'] == "Running":
        logging.info("Process still running, trying again in 10 seconds")
        time.sleep(10)
        check_status(status)
    elif status_response.status_code == 200 and body['runtimeStatus'] == "Completed":
        logging.info("Process completed, processing result")
        logging.info(f"Instance Id: {body['instanceId']}")
        return body
    else:
        logging.error("Return code or runtimeStatus not expected")


# Logging setup

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)])

response = send_text("A prompt goes here", API_ENDPOINT)
logging.info(f"Return code {response.status_code}")
if response.status_code == 202:
    id_no, status, terminate = get_links(response)
    reply_body = check_status(status)
    print(reply_body)
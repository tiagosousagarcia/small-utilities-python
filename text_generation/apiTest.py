import requests, time, logging, sys
# API_ENDPOINT = "http://localhost:7071/api/orchestrators/orchestrator-generation-test"

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
    if status_response.status_code == 202 and body['runtimeStatus'] == "Running" or body['runtimeStatus'] == "Pending":
        logging.info(f"Status code: {status_response.status_code}. Process still {body['runtimeStatus']}, trying again in 10 seconds")
        time.sleep(10)
        return check_status(status)
    elif status_response.status_code == 200 and body['runtimeStatus'] == "Completed":
        logging.info(f"Status code: {status_response.status_code}. Process completed, processing result")
        logging.info(f"Instance Id: {body['instanceId']}")
        logging.info(f"Output: {body['output']}")
        return body['output'], status_response.status_code
    else:
        logging.error("Return code or runtimeStatus not expected")
        return status_response.status_code



# Logging setup

# logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", handlers=[logging.FileHandler("API-debug.log"), logging.StreamHandler(sys.stdout)])

# Main

def start_generation(prompt, API_ENDPOINT):
    reply_result = ""
    response = send_text(prompt, API_ENDPOINT)
    logging.info(f"Return code {response.status_code}")
    if response.status_code == 202:
        id_no, status, terminate = get_links(response)
        reply_result, final_status = check_status(status)
    return reply_result, final_status


    
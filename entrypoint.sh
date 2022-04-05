#!/bin/bash
 
set -e


pip3 install -r /updateFC/requirements.txt

python3 /updateFC/UpdateAliyunFC.py --access-key-id "${INPUT_ACCESS_KEY_ID}" \
--access-key-secret "${INPUT_ACCESS_KEY_SECRET}" \
--account-ID "${INPUT_ACCOUNT_ID}" \
--server-name "${INPUT_SERVER_NAME}" \
--function-name "${INPUT_FUNCTION_NAME}" \
--region "${INPUT_REGION}" \
--repo-name "${INPUT_REPO_NAME}" \
--token "${INPUT_TOKEN}"

#!/bin/bash
 
set -e
 
if [ -z "$INPUT_ARGS" ]; then
  echo 'Required Args parameter'
  exit 1
fi

pip3 install -r /updateFC/requirements.txt

python3 /updateFC/UpdateAliyunFC.py --access_key_id "${INPUT_ACCESS_KEY}" \
--access_key_secret "${INPUT_ACCESS_KEY_SECRET}" \
--account_ID "${INPUT_ACCOUNT_ID}" \
--server_name "${INPUT_SERVER_NAME}" \
--function_name "${INPUT_FUNCTION_NAME}" \
--region "${INPUT_REGION}" 

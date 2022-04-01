#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/1 15:05 
# @Author : hesgang
# @File : UpdateFC.py 

import sys
import base64
import argparse
import yaml
from typing import List
from Tea.core import TeaCore

from alibabacloud_fc_open20210406.client import Client as FC_Open20210406Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_fc_open20210406 import models as fc__open_20210406_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


def _create_parser():
    with open('/action.yml', 'r') as f:
        action = yaml.safe_load(f)
    _parser = argparse.ArgumentParser(
        description=action['description'])
    inputs = action['inputs']

    for key in inputs:
        if key in ['dst_key']:
            continue
        input_args = inputs[key]
        dft = input_args.get('default', '')
        _parser.add_argument(
            "--" + key.replace('_', '-'),
            # Autofill the `type` according `default`, str by default
            type=str,
            required=input_args.get('required', False),
            default=dft,
            help=input_args.get('description', '')
        )
    return _parser


class UpdateFC:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
        account_id: str,
    ):
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = account_id + f".cn-beijing.fc.aliyuncs.com"
        return FC_Open20210406Client(config)

    @staticmethod
    def main(_ak, _sk, _accountid, _sever_name, _func_name, zipcode):
        client = UpdateFC.create_client(_ak, _accountid, _sk)
        update_function_headers = fc__open_20210406_models.UpdateFunctionHeaders()
        update_function_request = fc__open_20210406_models.UpdateFunctionRequest(code=zipcode)
        resp = client.update_function_with_options(_sever_name, _func_name, update_function_request, update_function_headers, util_models.RuntimeOptions())
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = UpdateFC.create_client('ACCESS_KEY_ID', 'ACCESS_KEY_SECRET')
        update_function_headers = fc__open_20210406_models.UpdateFunctionHeaders()
        update_function_request = fc__open_20210406_models.UpdateFunctionRequest()
        resp = await client.update_function_with_options_async('hepler', 'test', update_function_request, update_function_headers, util_models.RuntimeOptions())
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))


if __name__ == '__main__':
    file = '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'
    parser = _create_parser()
    args = parser.parse_args()

    # with open("test.zip", "rb") as f:
    #     by = f.read()
    #     encoded = base64.b64encode(by)
    #     f.close()
    #     print(encoded)
    zipfile = fc__open_20210406_models.Code(zip_file=file)
    UpdateFC.main(args.access_key_id, args.access_key_secret, args.account_ID, args.server_name, args.function_name, zipfile)

